from diagrams import Diagram, Cluster
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet, Firewall, Switch
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mysql
from diagrams.onprem.infra import Nginx
from diagrams.onprem.directory import ActiveDirectory

with Diagram("On-Prem Network Architecture", show=False, filename="onprem_network_architecture", direction="LR"):

    users = Users("Internal Users")
    internet = Internet("Internet")

    with Cluster("DMZ"):
        fw_dmz = Firewall("Firewall")
        web_server = Nginx("Web Server")
        fw_dmz >> web_server

    with Cluster("LAN"):
        switch = Switch("Core Switch")
        ad = ActiveDirectory("AD Server")
        file_server = Server("File Server")
        db_server = Mysql("Database Server")
        app_server = Server("App Server")

        switch >> [ad, file_server, db_server, app_server]

    users >> switch
    internet >> fw_dmz
    web_server >> app_server
    app_server >> db_server
