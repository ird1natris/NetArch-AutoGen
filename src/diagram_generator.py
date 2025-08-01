import os
import yaml
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, InternetGateway
from diagrams.aws.database import RDS
from typing import Dict, Any

def generate_diagram_from_yaml(data: Dict[str, Any], filename="outputs/sample"):
    title = data.get("title", "Network Architecture")

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with Diagram(title, filename=os.path.abspath(filename), outformat="png", show=False):
        nodes = {}

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

        for conn in data.get("connections", []):
            src = conn.get("from")
            dst = conn.get("to")
            if src in nodes and dst in nodes:
                nodes[src] >> nodes[dst]
