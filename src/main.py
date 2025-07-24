import argparse
import yaml
import os
from diagrams import Diagram
from diagrams.aws.network import VPC, InternetGateway, NATGateway, RouteTable

def parse_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def generate_diagram(config, output_path):
    print("✅ Generating diagram at:", output_path)
    with Diagram(config.get('title', 'Network Architecture'), show=False, outformat='png', filename=output_path.replace('.png', '')):
        # Basic AWS VPC architecture example
        igw = InternetGateway(config.get('internet_gateway', 'IGW'))
        vpc = VPC(config.get('vpc', 'VPC'))
        nat = NATGateway(config.get('nat_gateway', 'NAT'))
        rt = RouteTable(config.get('route_table', 'RouteTable'))

        igw >> vpc >> [nat, rt]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    # 🛠️ Ensure output folder exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # 🧠 Load config and generate diagram
    config = parse_config(args.config)
    print("📄 Parsed config:", config)
    generate_diagram(config, args.output)
