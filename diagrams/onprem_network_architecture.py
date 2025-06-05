from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet
from diagrams.generic.network import Router, Switch, Firewall
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql, Mysql
from diagrams.onprem.storage import Storage
from diagrams.custom import Custom

with Diagram("Complex On-Premises Network Architecture", show=False, filename="complex_onprem_network_architecture"):

    internet = Internet("Internet")

    with Cluster("Perimeter Network (DMZ)"):
        fw_dmz = Firewall("Firewall")
        lb = Custom("Load Balancer", "./icons/loadbalancer.png")  # Use a custom icon or just text node
        fw_dmz >> lb

    with Cluster("Internal Network"):
        fw_internal = Firewall("Internal Firewall")
        core_router = Router("Core Router")
        core_switch = Switch("Core Switch")

        with Cluster("Web Layer"):
            web_servers = [Server(f"Web Server {i}") for i in range(1, 4)]

        with Cluster("Application Layer"):
            app_servers = [Server(f"App Server {i}") for i in range(1, 3)]

        with Cluster("Database Layer"):
            db_master = Postgresql("PostgreSQL Master")
            db_slave = Mysql("MySQL Slave")

        storage = Storage("Network Storage")

        lb >> fw_internal
        fw_internal >> core_router
        core_router >> core_switch

        for ws in web_servers:
            core_switch >> ws

        for app in app_servers:
            core_switch >> app

        core_switch >> db_master
        core_switch >> db_slave
        db_master >> storage
        db_slave >> storage

    internet >> fw_dmz
