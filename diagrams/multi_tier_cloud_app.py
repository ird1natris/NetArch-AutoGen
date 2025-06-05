from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, Lambda, ECS
from diagrams.aws.network import ELB, Route53, VPC, PrivateSubnet, PublicSubnet
from diagrams.aws.database import RDS, ElastiCache, Dynamodb
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.security import WAF, Shield, IAM
from diagrams.onprem.client import Users
from diagrams.generic.network import Firewall

with Diagram("Multi-Tier Cloud App Architecture", show=False, outformat="png", filename="multi_tier_cloud_app"):

    users = Users("Users")
    internet = VPC("Internet")

    dns = Route53("DNS")
    waf = WAF("Web Application Firewall")
    shield = Shield("DDoS Protection")

    fw = Firewall("Perimeter Firewall")

    with Cluster("Public Subnet"):
        lb = ELB("Load Balancer")
        api_gateway = ELB("API Gateway")

    with Cluster("Private Subnet"):
        with Cluster("Compute Layer"):
            ecs_services = [ECS("Service A"), ECS("Service B"), ECS("Service C")]

        with Cluster("Data Layer"):
            rds = RDS("Relational DB")
            cache = ElasticCache("Redis Cache")
            dynamodb = Dynamodb("NoSQL DB")

    with Cluster("Messaging"):
        sqs = SQS("Queue")
        sns = SNS("Notification")

    iam = IAM("IAM Roles & Policies")

    # Connections
    users >> internet >> dns >> waf >> shield >> fw >> lb >> ecs_services
    ecs_services >> rds
    ecs_services >> cache
    ecs_services >> dynamodb
    ecs_services >> sqs >> sns
    iam >> ecs_services
