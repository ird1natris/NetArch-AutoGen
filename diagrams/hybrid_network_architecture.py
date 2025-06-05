from diagrams import Diagram, Cluster
from diagrams.generic.network import Router, Switch, Firewall, VPN
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile, Tablet  # Removed Laptop
from diagrams.aws.network import VPC, InternetGateway, PrivateSubnet, PublicSubnet
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.security import Shield

with Diagram("Hybrid Network Architecture", show=False, filename="hybrid-network-architecture", outformat="png"):

    users = [Mobile("Mobile User"), Tablet("Tablet User")]  # Removed Laptop User

    with Cluster("On-Prem Network"):
        onprem_router = Router("Edge Router")
        onprem_fw = Firewall("Firewall")
        onprem_switch = Switch("Core Switch")
        onprem_rack = Rack("App Server")
        onprem_db = Storage("On-Prem DB")

        onprem_router >> onprem_fw >> onprem_switch >> [onprem_rack, onprem_db]

    vpn_tunnel = VPN("VPN Tunnel")

    with Cluster("AWS Cloud"):
        igw = InternetGateway("Internet Gateway")
        shield = Shield("AWS Shield")

        with Cluster("VPC"):
            pub_subnet = PublicSubnet("Public Subnet")
            priv_subnet = PrivateSubnet("Private Subnet")

            ec2 = EC2("Web App")
            rds = RDS("Database")

            pub_subnet >> ec2
            priv_subnet >> rds

        vpc = VPC("Main VPC")
        vpc >> [pub_subnet, priv_subnet]

    # User access
    users >> onprem_router

    # On-prem to Cloud
    onprem_fw >> vpn_tunnel >> vpc

    # Internet to AWS
    igw >> shield >> ec2
