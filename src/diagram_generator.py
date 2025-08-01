import os
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, InternetGateway
from diagrams.aws.database import RDS
from typing import Dict, Any

def generate_diagram_from_yaml(data: Dict[str, Any], filename: str = "outputs/sample"):
    """
    Generate a network diagram from parsed YAML/JSON data.

    Args:
        data (dict): Parsed config data describing nodes and connections.
        filename (str): Output PNG filename path without extension.

    Returns:
        None
    """
    title = data.get("title", "Network Architecture")

    # Ensure output directory exists
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    nodes = {}

    with Diagram(title, filename=os.path.abspath(filename), outformat="png", show=False):
        # Create nodes
        for resource in data.get("resources", []):
            name = resource.get("name")
            r_type = resource.get("type", "").lower()

            if r_type == "ec2":
                nodes[name] = EC2(name)
            elif r_type == "elb":
                nodes[name] = ELB(name)
            elif r_type == "internet_gateway":
                nodes[name] = InternetGateway(name)
            elif r_type == "rds":
                nodes[name] = RDS(name)
            else:
                # fallback generic node
                nodes[name] = EC2(name)

        # Create connections
        for conn in data.get("connections", []):
            src = conn.get("from")
            dst = conn.get("to")
            if src in nodes and dst in nodes:
                nodes[src] >> nodes[dst]

    print(f"Diagram generated and saved to {filename}.png")

