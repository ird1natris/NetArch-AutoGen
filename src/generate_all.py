import os
import glob
import yaml
import json
from src.diagram_generator import generate_diagram_from_yaml

def main():
    os.makedirs("outputs", exist_ok=True)

    config_files = glob.glob("configs/*.yaml") + glob.glob("configs/*.yml") + glob.glob("configs/*.json")

    if not config_files:
        print("No config files found, skipping diagram generation.")
    else:
        for filepath in config_files:
            ext = os.path.splitext(filepath)[1].lower()
            with open(filepath) as f:
                if ext in ['.yaml', '.yml']:
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)
            base = os.path.splitext(os.path.basename(filepath))[0]
            print(f"Generating diagram from {filepath} -> outputs/{base}.png")
            generate_diagram_from_yaml(data, filename=f"outputs/{base}")

if __name__ == "__main__":
    main()
