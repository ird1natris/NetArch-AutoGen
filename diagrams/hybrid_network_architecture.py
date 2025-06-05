from diagrams import Diagram, Cluster
from diagrams.generic.network import Router, Switch, Firewall
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage
from diagrams.onprem.client import Users
from diagrams.aws.network import VPNConnection, VPC, InternetGateway, PrivateSubnet, PublicSubnet
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.client import Users
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.network import Internet

with Diagram("Hybrid On-Prem + Cloud Network Architecture", show=False, filename="hybrid-network-architecture", outformat="png"):

    internet = Internet("Internet")

    with Cluster("On-Premise"):
        firewall = Firewall("Firewall")
        router = Router("Router")
        switch = Switch("Core Switch")

        users = Users("Corporate Users")

        with Cluster("Internal Services"):
            ad = WindowsGeneral("Active Directory")
            db = SQL("On-Prem DB")
            web = Rack("Internal Web App")
            storage = Storage("File Server")

        monitoring = Prometheus("Monitoring")

    with Cluster("AWS Cloud"):
        igw = InternetGateway("Internet Gateway")
        vpc = VPC("VPC")

        with Cluster("Public Subnet"):
            ec2_web = EC2("Web Server")

        with Cluster("Private Subnet"):
            ec2_app = EC2("App Server")
            cloud_db = RDS("Cloud DB")

    # Connections
    internet >> firewall >> router >> switch
    switch >> users
    switch >> ad >> db >> web >> storage
    switch >> monitoring

    router >> VPNConnection("Site-to-Site VPN") >> igw >> vpc
    vpc >> [ec2_web, ec2_app] >> cloud_db
