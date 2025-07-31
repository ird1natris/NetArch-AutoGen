import yaml
from diagrams import Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.database import RDS
from diagrams.aws.integration import SQS
from diagrams.aws.security import WAF
from diagrams.onprem.client import Users

# Map custom YAML types to Diagrams library nodes
component_map = {
    "client": Users,
    "dns": Route53,
    "waf": WAF,
    "load_balancer": ELB,
    "compute": ECS,
    "database": RDS,
    "messaging": SQS
}

def generate_diagram_from_yaml(yaml_content: str, filename="outputs/generated_diagram"):
    data = yaml.safe_load(yaml_content)
    title = data.get("title", "Generated Architecture")
    components = {}
    
    with Diagram(title, show=False, filename=filename, outformat="png"):
        for comp in data["components"]:
            comp_type = comp["type"]
            comp_name = comp["name"]
            diagram_node = component_map.get(comp_type)
            if diagram_node:
                components[comp_name] = diagram_node(comp_name)

        for conn in data["connections"]:
            src = components.get(conn["from"])
            tgt = components.get(conn["to"])
            if src and tgt:
                src >> tgt
