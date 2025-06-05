from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC, InternetGateway, NATGateway, ELB
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.general import Client
from diagrams.aws.security import Shield
from diagrams.onprem.network import VPN

with Diagram("Advanced Network Architecture", show=False, outformat="png", filename="complex_network_diagram"):

    vpn = VPN("On-Prem VPN")

    with Cluster("VPC"):
        igw = InternetGateway("Internet Gateway")
        nat = NATGateway("NAT Gateway")

        with Cluster("Public Subnet"):
            lb = ELB("Load Balancer")
            web = [EC2("Web1"), EC2("Web2")]

        with Cluster("Private Subnet - App Tier"):
            app_asg = AutoScaling("App Tier")

        with Cluster("Private Subnet - Database Tier"):
            db = RDS("Primary DB")

        # Connectivity
        vpn >> igw >> lb >> web
        lb >> app_asg >> db
        app_asg >> nat
