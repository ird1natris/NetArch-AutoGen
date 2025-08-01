import os
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, InternetGateway
from diagrams.aws.database import RDS

def generate_diagram_from_yaml(data, filename="outputs/sample"):
    """
    Generate a diagram PNG from YAML/JSON data.

    Args:
        data (dict): Parsed YAML/JSON dictionary describing resources and connections.
        filename (str): Output file path without extension. PNG will be saved here.
    """
    title = data.get("title", "Network Architecture")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with Diagram(title, filename=os.path.abspath(filename), outformat="png", show=False):
        nodes = {}

        # Create nodes based on resources
        for resource in data.get("resources", []):
            name = resource.get("name")
            r_type = resource.get("type")

            if r_type == "ec2":
                nodes[name] = EC2(name)
            elif r_type == "elb":
                nodes[name] = ELB(name)
            elif r_type == "internet_gateway":
                nodes[name] = InternetGateway(name)
            elif r_type == "rds":
                nodes[name] = RDS(name)
            else:
                nodes[name] = EC2(name)  # fallback

        # Create connections between nodes
        for conn in data.get("connections", []):
            src = conn.get("from")
            dst = conn.get("to")
            if src in nodes and dst in nodes:
                nodes[src] >> nodes[dst]
