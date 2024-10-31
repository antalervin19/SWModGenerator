# Stormworks Mod Structure Generator

This is a simple command-line tool for generating mod folder structures for Stormworks. The tool automatically creates a mod folder with subdirectories and a `mod.xml` file based on user-provided information, making it easier to set up and organize new mods.

## Features

- Automatically generates a mod folder with the specified name.
- Creates audio, data, graphics, and meshes subdirectories.
- Generates a mod.xml file with the mod's name, author, and description.

## Prerequisites

To build the tool from the Python script, you need:
- Python 3.x installed on your system.
- auto-py-to-exe package to compile the .py script into an .exe file.

## Installation

1. **Clone or download this repository.**
2. **Install auto-py-to-exe** (used to compile the Python script):

   `pip install auto-py-to-exe`

3. **Compile the Python script into an executable**:

   Run `auto-py-to-exe` and configure it as follows:
   - Select the script (ModGen.py) as the script file.
   - Choose "One file" for packaging the .exe.
   - Set it to "Console Based" since this is a command-line tool.
   - Click "Convert .py to .exe" to generate the ModGen.exe file.

4. **Locate ModGen.exe in the output directory** specified in auto-py-to-exe.

## Usage

After compiling, you can use `ModGen.exe` directly from the command line to generate mod folder structures.

### Basic Command Structure

`ModGen.exe -o "<output_path>" -n "<mod_name>" -d "<mod_description>" [-a "<author_name>"]`

### Options

- `-o` or `--output` (required): The output path where the mod folder will be created.
- `-n` or `--name` (required): The name of the mod, which will also be the folder name.
- `-d` or `--description` (required): A description of the mod.
- `-a` or `--author` (optional): The author of the mod. Defaults to `"Unknown"` if not provided.
- `-h` or `--help`: Displays help information.

### Example Usage

1. **Basic example with required arguments**:

   `ModGen.exe -o "%AppData%\Stormworks\data\mods" -n "NewMod" -d "Description for the mod"`

2. **Full example including the author**:

   `ModGen.exe -o "%AppData%\Stormworks\data\mods" -n "NewMod" -d "Description for the mod" -a "My mods author"`

### Generated Structure

Running the tool will generate a folder with this structure:
```
<output_path> 
└── NewMod
   ├── audio
   ├── data
   ├── graphics
   ├── meshes
   └── mod.xml
```

The `mod.xml` file will contain the following structure:
