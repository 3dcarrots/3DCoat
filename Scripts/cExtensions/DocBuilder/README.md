# DocBuilder Extension for 3DCoat

DocBuilder is an extension for 3DCoat and 3DCoat Textura that automates the documentation generation process for the 3DCoat Python API. It uses the Sphinx documentation generator to create convenient HTML pages based on the source code (including `cPy`, `cModules`, and `cTemplates`).

## Features
- Automatic generation of 3DCoat API documentation directly from the application.
- Support for the `pydata-sphinx-theme` to create a modern and convenient documentation layout.
- Smart parsing: the `sphinx_builder.py` script automatically scans the code, collects docstrings, and adds links to classes and methods (autolinking).

## Installation

To install the extension, you need to extract the `DocBuilder` folder into your program's scripts directory.

- **For 3DCoat:**
  Copy the `DocBuilder` folder to the following path:
  `Documents\3DCoat2026\UserPrefs\Scripts\cExtensions\DocBuilder`

- **For 3DCoat Textura:**
  Copy the `DocBuilder` folder to the following path:
  `Documents\3DCoatTextura\UserPrefs\Scripts\cExtensions\DocBuilder`

Restart 3DCoat after copying.

## Requirements

All required dependencies (such as `sphinx`, `pydata-sphinx-theme`, `sphinx-gallery`, and `pyenchant`) are handled and automatically installed by 3DCoat internally. You do not need to manually install them via `pip`.

## Usage

1. Launch 3DCoat or 3DCoat Textura.
2. In the main top menu, navigate to **Scripts -> Useful**.
3. Click on **RebuildDocumentation**.
4. The extension will start the generation process. Once complete, the generated HTML documentation will be located in the `UserPrefs/PythonAPI/docs/build` folder.
