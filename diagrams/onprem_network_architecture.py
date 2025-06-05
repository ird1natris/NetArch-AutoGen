from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet, Router
from diagrams.generic.network import Firewall
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql, Mysql
from diagrams.onprem.storage import Storage

with Diagram("Complex On-Premises Network Architecture", show=False, filename="complex_onprem_network_architecture"):

    internet = Internet("Internet")

    with Cluster("Perimeter Network (DMZ)"):
        fw_dmz = Firewall("Firewall")
        # LoadBalancer replacement: use Router as a placeholder
        lb = Router("Load Balancer (Router)")
        fw_dmz >> lb

    with Cluster("Internal Network"):
        fw_internal = Firewall("Internal Firewall")
        internal_router = Router("Core Router")

        with Cluster("Web Layer"):
            web_servers = [Server(f"Web Server {i}") for i in range(1, 4)]

        with Cluster("Application Layer"):
            app_servers = [Server(f"App Server {i}") for i in range(1, 3)]

        with Cluster("Database Layer"):
            db_master = Postgresql("PostgreSQL Master")
            db_slave = Mysql("MySQL Slave")

        storage = Storage("Network Storage")

        lb >> fw_internal
        fw_internal >> internal_router

        for ws in web_servers:
            internal_router >> ws

        for app in app_servers:
            internal_router >> app

        internal_router >> db_master
        internal_router >> db_slave
        db_master >> storage
        db_slave >> storage

    internet >> fw_dmz
