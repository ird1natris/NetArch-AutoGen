from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet, Switch, Router, LoadBalancer
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql, Mysql
from diagrams.onprem.storage import Storage
from diagrams.generic.network import Firewall

with Diagram("Complex On-Premises Network Architecture", show=False, filename="complex_onprem_network_architecture"):

    internet = Internet("Internet")

    with Cluster("Perimeter Network (DMZ)"):
        fw_dmz = Firewall("Firewall")
        lb = LoadBalancer("Load Balancer")
        dmz_switch = Switch("DMZ Switch")
        fw_dmz >> lb >> dmz_switch

    with Cluster("Internal Network"):
        fw_internal = Firewall("Internal Firewall")
        internal_router = Router("Core Router")
        internal_switch = Switch("Internal Switch")

        # Servers
        with Cluster("Web Layer"):
            web_servers = [Server(f"Web Server {i}") for i in range(1, 4)]

        with Cluster("Application Layer"):
            app_servers = [Server(f"App Server {i}") for i in range(1, 3)]

        with Cluster("Database Layer"):
            db_master = Postgresql("PostgreSQL Master")
            db_slave = Mysql("MySQL Slave")

        # Storage
        storage = Storage("Network Storage")

        # Connections
        dmz_switch >> fw_internal
        fw_internal >> internal_router >> internal_switch

        for ws in web_servers:
            internal_switch >> ws >> Edge(color="brown", style="dashed") >> lb  # Web servers connect back to load balancer

        for app in app_servers:
            internal_switch >> app

        internal_switch >> db_master
        internal_switch >> db_slave
        db_master >> storage
        db_slave >> storage

    internet >> fw_dmz
