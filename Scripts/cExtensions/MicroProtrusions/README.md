# MicroProtrusions Extension for 3DCoat

MicroProtrusions is a powerful tool (filter) for 3DCoat and 3DCoat Textura, designed for advanced processing of maps (Albedo, Gloss, etc.) based on a relief map (Height Map or Normal Map). The extension allows you to, for example, emphasize the highest peaks of the relief or accurately displace the pixels of the target textures based on the normal map vectors.

## Features
- **Height Map Mode:** Allows you to isolate and preserve texture details primarily on the highest points of the relief (by adjusting the Weight/Power).
- **Normal Map Mode:** Displaces pixels of the target map according to normal vectors by a specified distance (Displacement Distance).
- Ability to downsample target maps (from 1x to 32x) for optimization.
- Support for green channel inversion (Invert Y) for normal maps.
- Batch processing (add multiple target textures at once for simultaneous processing).

## Installation

To install the extension, you need to extract the `MicroProtrusions` folder into your program's scripts directory.

- **For 3DCoat:**
  Copy the `MicroProtrusions` folder to the following path:
  `Documents\3DCoat2026\UserPrefs\Scripts\cExtensions\MicroProtrusions`

- **For 3DCoat Textura:**
  Copy the `MicroProtrusions` folder to the following path:
  `Documents\3DCoatTextura\UserPrefs\Scripts\cExtensions\MicroProtrusions`

Restart 3DCoat after copying.

## Usage

1. Launch 3DCoat or 3DCoat Textura.
2. In the main top menu, navigate to **Scripts -> Useful**.
3. Click on **OpenMicroProtrusionsUI**.
4. In the extension window:
   - Select the type of relief map (*Height Map* or *Normal Map*).
   - Load the corresponding relief map (`Load Relief Map...`).
   - Add the target maps you want to process, such as Albedo or Roughness (`Add Target Maps...`).
   - Adjust the processing parameters (downsampling, displacement distance, etc.).
   - Click **Process & Save Maps** and choose a folder to save the newly generated textures.

## Requirements
- 3DCoat 2026 (or 3DCoat Textura)
- The required Python modules (`numpy`, `cv2`, `Pillow`) will be automatically installed by 3DCoat.
