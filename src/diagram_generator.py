import os
import datetime
import random
import string
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, InternetGateway
from diagrams.aws.database import RDS

def generate_diagram_from_yaml(data, filename="outputs/sample"):
    try:
        # Ensure the output folder exists
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)

        title = data.get("title", "Network Architecture")
        filepath = os.path.abspath(filename)

        with Diagram(title, filename=filepath, outformat="png", show=False):
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
                    nodes[name] = EC2(name)  # fallback node

            for conn in data.get("connections", []):
                src = conn.get("from")
                dst = conn.get("to")
                if src in nodes and dst in nodes:
                    nodes[src] >> nodes[dst]

        output_file = filepath + ".png"
        if not os.path.isfile(output_file):
            raise FileNotFoundError(f"Diagram file not found at {output_file}")

        return output_file

    except Exception as e:
        # Create unique fallback folder like outputs/generated_20250801_1425 or random suffix
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fallback_folder = f"outputs/generated_{timestamp}"
        os.makedirs(fallback_folder, exist_ok=True)
        fallback_path = os.path.abspath(os.path.join(fallback_folder, "generated"))

        with Diagram("Generated Fallback", filename=fallback_path, outformat="png", show=False):
            internet = InternetGateway("Internet")
            ec2 = EC2("Fallback EC2")
            rds = RDS("Fallback RDS")
            internet >> ec2 >> rds

        return fallback_path + ".png"
