import yaml
import json
from typing import Dict, Any

def parse_config(path: str) -> Dict[str, Any]:
    """
    Parse YAML or JSON config file and return as dict.

    Args:
        path (str): Path to the config file.

    Returns:
        Dict[str, Any]: Parsed config dictionary.

    Raises:
        ValueError: If file format is unsupported.
        FileNotFoundError: If file does not exist.
    """
    if path.endswith(('.yml', '.yaml')):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    elif path.endswith('.json'):
        with open(path, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported config format. Use YAML or JSON.")
