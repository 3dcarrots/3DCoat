import coat
coat.run_extension("RealityCapture", True)
coat.ui.toRoom("Photogrammetry", True)
coat.ui.cmd("$PhotogrammetryTool")
coat.ui.wait("$COMBOBOX_PHOTOGRAMMETRY_ENGINERealityCapture", 1)
coat.ui.cmd("$COMBOBOX_PHOTOGRAMMETRY_ENGINERealityCapture")