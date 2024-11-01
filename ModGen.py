import os
import argparse
import xml.etree.ElementTree as ET

def GenerateModFolder(output_path, name, description, author="Unknown"):
    mod_folder_path = os.path.join(output_path, name)
    os.makedirs(mod_folder_path, exist_ok=True)
    
    subfolders = ["audio", "data", "graphics", "meshes"]
    for subfolder in subfolders:
        os.makedirs(os.path.join(mod_folder_path, subfolder), exist_ok=True)
    
    data_folder_path = os.path.join(mod_folder_path, "data")
    definitions_folder_path = os.path.join(data_folder_path, "definitions")
    os.makedirs(definitions_folder_path, exist_ok=True)
    
    mod_xml_path = os.path.join(mod_folder_path, "mod.xml")
    
    root = ET.Element("mod", name=name, author=author, desc=description)
    tree = ET.ElementTree(root)

    tree.write(mod_xml_path, encoding="UTF-8", xml_declaration=True)
    print(f"Mod structure created successfully at {mod_folder_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Stormworks mod folder structure with mod.xml")

    parser.add_argument("-o", "--output", required=True, help="Specify the output path where the mod folder will be created")
    parser.add_argument("-n", "--name", required=True, help="Specify the name of the mod (this will be the folder name)")
    parser.add_argument("-d", "--description", required=True, help="Provide a description for the mod")
    parser.add_argument("-a", "--author", default="Unknown", help="(Optional) Specify the author of the mod")
    
    args = parser.parse_args()
    GenerateModFolder(args.output, args.name, args.description, args.author)

if __name__ == "__main__":
    main()
