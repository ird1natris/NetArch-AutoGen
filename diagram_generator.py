from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
import yaml
import json
import tempfile
import os

def generate_diagram(file_path: str) -> str:
    # Load file (YAML or JSON)
    with open(file_path, 'r') as f:
        if file_path.endswith((".yaml", ".yml")):
            config = yaml.safe_load(f)
        elif file_path.endswith(".json"):
            config = json.load(f)
        else:
            raise ValueError("Unsupported file format")

    # Example only — feel free to expand based on config
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        output_path = tmpfile.name

    with Diagram("Generated Diagram", show=False, outformat="png", filename=output_path.replace(".png", "")):
        lb = ELB("Load Balancer")
        ec2_1 = EC2("Web 1")
        ec2_2 = EC2("Web 2")
        lb >> [ec2_1, ec2_2]

    return output_path
