import os
import sys
import yaml
import json
from diagram_generator import generate_diagram_from_yaml

def main():
    # Get absolute path to project root
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Absolute paths to folders
    config_folder = os.path.join(ROOT_DIR, 'configs')
    output_folder = os.path.join(ROOT_DIR, 'outputs')
    
    os.makedirs(output_folder, exist_ok=True)

    # Collect config files
    files = []
    for f in os.listdir(config_folder):
        if f.endswith((".yaml", ".yml", ".json")):
            files.append(os.path.join(config_folder, f))

    if not files:
        print("No config files found in 'configs/' folder.")
        return

    for filepath in files:
        print(f"Processing {filepath} ...")
        try:
            with open(filepath) as f:
                ext = os.path.splitext(filepath)[1].lower()
                data = yaml.safe_load(f) if ext in [".yaml", ".yml"] else json.load(f)

            filename = os.path.join(output_folder, os.path.splitext(os.path.basename(filepath))[0])
            generate_diagram_from_yaml(data, filename=filename)
            print(f"✅ Diagram saved to {filename}.png\n")
        except Exception as e:
            print(f"❌ Failed to process {filepath}: {e}")

if __name__ == "__main__":
    main()
