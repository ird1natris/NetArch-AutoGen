import argparse
from config_parser import parse_config
from diagram_generator import generate_diagram
import logging
import sys

def main():
    parser = argparse.ArgumentParser(description="NetArch-AutoGen: Generate network diagrams from config files")
    parser.add_argument('--config', '-c', required=True, help="Path to YAML/JSON config file")
    parser.add_argument('--output', '-o', required=True, help="Output PNG file path")

    args = parser.parse_args()

    try:
        config = parse_config(args.config)
    except Exception as e:
        logging.error(f"Failed to parse config: {e}")
        sys.exit(1)

    try:
        generate_diagram(config, args.output)
    except Exception as e:
        logging.error(f"Failed to generate diagram: {e}")
        sys.exit(1)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
