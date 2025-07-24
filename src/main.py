import argparse
import yaml
import os
from diagrams import Diagram
from diagrams.aws.network import VPC, InternetGateway, NATGateway, RouteTable

def parse_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def generate_diagram(config, output_path):
    with Diagram(config.get('title', 'Network Architecture'), show=False, outformat='png', filename=output_path.replace('.png', '')):
        # Basic AWS VPC architecture
        igw = InternetGateway(config['internet_gateway'])
        vpc = VPC(config['vpc'])
        nat = NATGateway(config['nat_gateway'])
        rt = RouteTable(config['route_table'])

        igw >> vpc >> [nat, rt]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    config = parse_config(args.config)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    generate_diagram(config, args.output)
