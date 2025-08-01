import sys
import os
import yaml
import json
from src.diagram_generator import generate_diagram_from_yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    config_folder = "configs"
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)

    # List all yaml, yml, json files in configs/
    files = []
    for ext in ("*.yaml", "*.yml", "*.json"):
        files.extend(os.path.join(config_folder, f) for f in os.listdir(config_folder) if f.endswith(ext[1:]))

    if not files:
        print("No config files found in 'configs/' folder.")
        return

    for filepath in files:
        print(f"Processing {filepath} ...")
        try:
            with open(filepath) as f:
                ext = os.path.splitext(filepath)[1].lower()
                if ext in [".yaml", ".yml"]:
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)

            filename = os.path.join(output_folder, os.path.splitext(os.path.basename(filepath))[0])
            generate_diagram_from_yaml(data, filename=filename)
            print(f"Diagram saved to {filename}.png\n")
        except Exception as e:
            print(f"Failed to process {filepath}: {e}")

if __name__ == "__main__":
    main()
