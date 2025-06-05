from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import ELB, Route53, CloudFront
from diagrams.aws.security import WAF, KMS, Shield
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet
from diagrams.generic.network import Firewall
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile  # Used instead of Stripe & Okta

with Diagram("Banking Sector Network Architecture", show=False, outformat="png", filename="banking_network_diagram"):

    users = Users("Bank Customers")
    internet = Internet("Internet")
    waf = WAF("Web App Firewall")
    dns = Route53("DNS")
    cdn = CloudFront("CDN")
    fw = Firewall("Perimeter Firewall")

    with Cluster("Public Zone"):
        lb = ELB("App Load Balancer")
        api_lb = ELB("API Gateway LB")

        web_servers = [EC2("WebApp-1"), EC2("WebApp-2")]
        api_servers = [EC2("API-1"), EC2("API-2")]

    with Cluster("DMZ"):
        ids = Shield("Intrusion Detection")
        proxy = EC2("Secure Proxy")

    with Cluster("Internal Core Banking Zone"):
        with Cluster("Microservices Tier"):
            services = [Lambda("Account Svc"), Lambda("Transaction Svc"), Lambda("Loan Svc")]

        with Cluster("Database Tier"):
            core_db = RDS("Core Banking DB")
            analytics_db = Dynamodb("Analytics DB")

        kms = KMS("Tokenization/KMS")

    with Cluster("3rd Party Integrations"):
        stripe = Mobile("Payment Gateway")  # Generic icon instead of Stripe
        okta = Mobile("Identity Provider")  # Generic icon instead of Okta
        credit_api = EC2("Credit Bureau API")
        storage = Storage("Document Storage")

    # Connections
    users >> internet >> dns >> cdn >> waf >> fw >> lb >> web_servers
    users >> internet >> dns >> cdn >> waf >> fw >> api_lb >> api_servers
    web_servers >> proxy >> ids >> services
    api_servers >> proxy >> ids >> services
    services >> core_db
    services >> analytics_db
    services >> kms

    services >> stripe
    services >> credit_api
    services >> storage
    users >> okta >> api_lb
