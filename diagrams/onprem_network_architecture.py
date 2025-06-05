from diagrams import Diagram, Cluster
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mysql
from diagrams.onprem.directory import ActiveDirectory
from diagrams.onprem.security import Iptables, Opnsense

with Diagram("On-Prem Network Architecture", show=False, filename="onprem_network_architecture", direction="LR"):

    users = Users("Internal Users")
    internet = Internet("Internet")

    with Cluster("DMZ"):
        firewall = Iptables("Firewall")
        web = Server("Nginx Web Server")  # Use Server as stand-in for Nginx
        firewall >> web

    with Cluster("LAN"):
        opnsense = Opnsense("OpnSense (Router/Switch Alt)")
        ad = ActiveDirectory("AD Server")
        file_server = Server("File Server")
        db = Mysql("Database")
        app_server = Server("App Server")

        opnsense >> [ad, file_server, db, app_server]

    users >> opnsense
    internet >> firewall
    web >> app_server
    app_server >> db
