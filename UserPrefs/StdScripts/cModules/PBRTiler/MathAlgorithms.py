import numpy as np

def calculate_homography(source_pts, dest_pts):
    """
    Constructs the 8-parameter Homography matrix (H)
    source_pts: [(u1, v1), (u2, v2), (u3, v3), (u4, v4)]
    dest_pts: [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    Returns the mapping matrix transforming Dest to Source.
    """
    A = []
    b = []
    for (u, v), (x, y) in zip(source_pts, dest_pts):
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y])
        b.append(u)
        b.append(v)
    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    
    try:
        h = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        # Fallback to identity matrix on singular
        return np.eye(3, dtype=np.float32)
        
    H_inv = np.array([
        [h[0], h[1], h[2]],
        [h[3], h[4], h[5]],
        [h[6], h[7], 1.0]
    ], dtype=np.float32)
    
    return H_inv

def frankot_chellappa(np_normal_map):
    """
    Frankot-Chellappa algorithm to convert a Normal map to a Height map.
    np_normal_map: numpy array shape (H, W, 3) in range [0, 1]
    Returns: Height map numpy array shape (H, W) mapped roughly to [0, 1]
    """
    # normal_map is expected to be RGB [0..1]
    nx = (np_normal_map[:, :, 0] - 0.5) * 2.0
    ny = (np_normal_map[:, :, 1] - 0.5) * 2.0
    nz = (np_normal_map[:, :, 2] - 0.5) * 2.0
    
    # Ensure no division by zero
    nz = np.maximum(nz, 1e-5)
    
    # Gradients p and q
    p = -nx / nz
    q = ny / nz # OpenGL format assumption
    
    # CRITICAL: Eliminate global tilt (DC bias).
    # If the mean gradient isn't exactly zero, FFT assumes a non-periodic ramp,
    # causing severe low-frequency gradients and spectral leakage.
    p = p - np.mean(p)
    q = q - np.mean(q)
    
    rows, cols = p.shape
    
    # FFT of gradients
    P = np.fft.fft2(p)
    Q = np.fft.fft2(q)
    
    # Create frequency grids
    wx = np.fft.fftfreq(cols) * 2 * np.pi
    wy = np.fft.fftfreq(rows) * 2 * np.pi
    
    Wx, Wy = np.meshgrid(wx, wy)
    
    # Frankot Chellappa equation
    denom = Wx**2 + Wy**2
    denom[0, 0] = 1.0 # Avoid division by zero at DC
    
    Z = (-1j * Wx * P - 1j * Wy * Q) / denom
    Z[0, 0] = 0.0 # DC component
    
    # Inverse FFT
    z_spatial = np.fft.ifft2(Z).real
    
    # Normalize to [0, 1]
    z_min = z_spatial.min()
    z_max = z_spatial.max()
    if z_max > z_min:
        z_spatial = (z_spatial - z_min) / (z_max - z_min)
        
    return z_spatial

def calculate_seam_energy_offset(luma_map):
    """
    Uses Phase Correlation / FFT to find optimal tiling offset.
    luma_map: 2D array [0,1]
    Returns optimal (dx, dy) offset (normalized 0..1)
    """
    # Standard Phase Correlation for demonstration
    # In a full production system, this would evaluate toroidal seam energy
    rows, cols = luma_map.shape
    G_a = np.fft.fft2(luma_map)
    G_b = np.conjugate(G_a)
    
    R = (G_a * G_b) / np.abs(G_a * G_b + 1e-8)
    r = np.fft.ifft2(R).real
    
    # Find peak
    peak_y, peak_x = np.unravel_index(np.argmax(r), r.shape)
    
    return float(peak_x) / cols, float(peak_y) / rows
