# 3D-Coat AppLinks Specifications

[cite_start]**(Applicable to version 4.8.15 and later)** [cite: 3]
[cite_start]**(Document based on 3D-Coat AppLinks specifications dated April 6, 2018)** [cite: 2]

[cite_start]AppLinks are plugins written for specific applications, intended to simplify data exchange between those applications and 3D-Coat[cite: 4, 5].

***

## 1. The Exchange Path

[cite_start]Your plugin must compose the path for data exchange[cite: 7]. [cite_start]The base structure is[cite: 8]:

`My Documents\AppLinks\3D-Coat\Exchange\`

[cite_start]This full path is referred to as **`exchange_path`**[cite: 13].

### Obtaining `exchange_path` by OS:

| OS | Method | Path Suffix |
| :--- | :--- | :--- |
| **Windows** | Use `SHGetFolderPath` with `CSIDL_PERSONAL \| [cite_start]CSIDL_FLAG_CREATE`[cite: 205]. | [cite_start]Append `AppLinks/3D-Coat/Exchange/`[cite: 207]. |
| **OSX** | [cite_start]Use `FSFindFolder` with `kUserDomain, kCurrentUserFolderType, kCreateFolder`[cite: 193]. | [cite_start]Append `AppLinks/3D-Coat/Exchange/`[cite: 196]. |
| **Linux** | [cite_start]Start with the home directory (e.g., using `g_get_home_dir()`)[cite: 200]. | [cite_start]Append `AppLinks/3D-Coat/Exchange/`[cite: 202]. |

> [cite_start]**Note:** Paths should preferably use **`/`** instead of **`\`**[cite: 95].

***

## 2. Listing AppLinks in `File -> Export To ->`

[cite_start]To make your application appear in 3D-Coat's `File -> Export To ->` menu[cite: 14, 17]:

1.  [cite_start]**Create a Folder:** Create a folder corresponding to your application name (e.g., `Blender`) inside the `exchange_path` (e.g., `exchange_path/Blender`)[cite: 15, 16].
2.  **Required and Optional Files:**

| File | Status | Description |
| :--- | :--- | :--- |
| **`run.txt`** | [cite_start]**Mandatory** [cite: 20] | [cite_start]Must exist[cite: 20]. [cite_start]If it contains a path to an executable, that file will run when the user selects the AppLink menu item[cite: 20]. |
| **`extension.txt`** | [cite_start]Optional [cite: 21] | Contains the file extension for export. [cite_start]If the file does not exist, **OBJ** is used[cite: 22]. |
| **`params.txt`** | [cite_start]Optional [cite: 23] | [cite_start]Parameters passed to the executable specified in `run.txt`, excluding the path to the object[cite: 24]. |
| **`preset.txt`** | [cite_start]Optional [cite: 25] | [cite_start]The name of the export preset 3D-Coat will use[cite: 26]. |
| **`*.xml`** | [cite_start]Optional [cite: 27] | [cite_start]Any XML file here is treated as an export preset, copied to the presets folder, and used as the default preset for this AppLink[cite: 28, 29]. |

***

## 3. AppLink Scenarios

### Scenario 1: Application → 3D-Coat and Back

[cite_start]This scenario is for sending an object from your application to 3D-Coat for editing and receiving it back[cite: 33].

#### Part 1: Application to 3D-Coat (Initiate Import)

1.  [cite_start]**Export Object:** The plugin exports the object from the application to `exchange_path` (e.g., `exchange_path/exportfile.obj`)[cite: 35, 36].
2.  [cite_start]**Define Return Path:** Decide the path for the final file 3D-Coat will create (e.g., `exchange_path/returnpath.obj`)[cite: 37].
3.  [cite_start]**Create `import.txt`:** Create the file `import.txt` in the `exchange_path`[cite: 38]. [cite_start]**The creation of this file signals 3D-Coat to start importing**[cite: 99].

    [cite_start]The general format for a single line in `import.txt` is[cite: 39]:
    ```
    path/to/exported/object ,path/to/return/object ,"[import_mode] ","[export_preset_name] " [script_commands]
    ```

    **Example:**
    ```
    [cite_start]exchange_path/exportfile.obj ,exchange_path/returnpath.obj ,"[ppp] ","[export_preset Blender Cycles] " [cite: 39]
    ```

    [cite_start]**Multiple objects** can be imported simultaneously by separating their paths with a semicolon `;`[cite: 144, 145].

    **Import Modes (`[import_mode]` examples):**
    * [cite_start]`[ppp]` — Per-pixel painting[cite: 40, 42].
    * [cite_start]`[mv]` — Microvertex painting[cite: 43].
    * [cite_start]`[vox]` — Drop as a voxel object[cite: 48].
    * [cite_start]`[uv]` — Perform UV-mapping[cite: 45].
    * [cite_start]`[retopo]` — Drop as a new retopo layer[cite: 47].
    * [cite_start]`[autopo]` — Drop mesh for Auto-retopology[cite: 53].

    [cite_start]**Additional Commands in `import.txt` (via extra lines)[cite: 262]:**
    * [cite_start]`[SkipImport]` — Skips the import dialog, using default options[cite: 263].
    * [cite_start]`[SkipExport]` — Skips the export dialog, using previous settings (4.8.16 and later)[cite: 264].
    * [cite_start]`[TexOutput:… texture path here…]` — Specifies the texture output path (must end with `\` or `/`)[cite: 265].
    * [cite_start]`[script text_of_script]` — Runs an inline script after importing the object[cite: 57, 59].
    * [cite_start]`[scriptfile path_to_script_file]` — Runs a script from a file (the file must contain `main(){...}`)[cite: 61, 62].

#### Part 2: 3D-Coat Back to Application (Receive Export)

1.  [cite_start]**User Action:** The user selects **`File -> Open in original App`** in 3D-Coat[cite: 103].
2.  **3D-Coat Creates Files (Signals):**
    * [cite_start]**`exchange_path/export.txt`** — Contains the path to the exported model file (the return path defined in `import.txt`)[cite: 105, 106].
    * [cite_start]**`exchange_path/textures.txt`** — Contains references to the exported textures[cite: 109]. [cite_start]Texture data is listed in sets of four lines[cite: 110, 111, 112, 113]:
        1.  [cite_start]Name\_of\_material\_1 [cite: 110]
        2.  [cite_start]Name\_of\_uv\_set\_1 [cite: 111]
        3.  [cite_start]Texure\_usage\_1 (e.g., `diffuse`, `normal_map`, `reflection`) [cite: 112, 116]
        4.  [cite_start]Absolute\_path\_to\_texture\_1 [cite: 113]
3.  **Plugin Action:**
    * [cite_start]Monitor for the existence of **`export.txt`**[cite: 119].
    * [cite_start]Read the content of `export.txt` and `textures.txt`[cite: 119, 131].
    * [cite_start]**The plugin must delete `export.txt` and `textures.txt` after reading**[cite: 119, 179].

### Scenario 2: 3D-Coat → Application (Export via Menu)

[cite_start]This scenario is triggered when the user selects an AppLink from the `File -> Export To ->` menu[cite: 124, 125].

1.  **3D-Coat Creates Files (Signals):**
    * [cite_start]**`exchange_path/YourAppName/export.txt`** — Contains the path of the exported object[cite: 126, 128].
    * [cite_start]**`exchange_path/textures.txt`** — Contains the list of exported textures[cite: 130].

    > [cite_start]**Note:** The `export.txt` file is in your application's subfolder, while `textures.txt` is in the main `exchange_path`[cite: 132].

2.  **Plugin Action:**
    * [cite_start]Monitor for the appearance of `export.txt` in your application's folder (`exchange_path/YourAppName/`)[cite: 127].
    * [cite_start]Read the object path from `export.txt` and the texture list from `textures.txt`[cite: 128, 131].
    * [cite_start]**The plugin must delete `export.txt` after reading**[cite: 129].

***

## General Plugin Architecture

[cite_start]The suggested general architecture for a plugin is[cite: 209]:

### [cite_start]1. Initialisation Section [cite: 210]
* [cite_start]Get and store the `exchange_path`[cite: 211].
* [cite_start]Create the folder `Exchange/YourApp/`[cite: 212].
* [cite_start]Create the mandatory file `run.txt` and the optional file `params.txt`[cite: 212].
* [cite_start]Create a timer or thread to check for the existence of `import.txt` (if available)[cite: 213].

### [cite_start]2. Processing Section (Monitoring) [cite: 214]
* [cite_start]Periodically (e.g., once every 1 second) check if the following files exist[cite: 215]:
    * `Exchange/import.txt`
    * `Exchange/YourApp/export.txt`
* [cite_start]It is helpful (but not required) for the plugin to check if the "3D-Coat" process is running and suggest the user run it if it is not found (by seeking a process with the substring “3D-Coat”)[cite: 219, 220].