from diagrams import Cluster, Diagram
from diagrams.generic.network import Router, Switch, Firewall
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql
from diagrams.onprem.network import Internet
from diagrams.custom import Custom

with Diagram("On-Prem Network Architecture", show=False):

    internet = Internet("Internet")

    with Cluster("Edge"):
        edge_fw = Firewall("Edge Firewall")
        edge_router = Router("Edge Router")

    with Cluster("DMZ"):
        dmz_fw = Firewall("DMZ Firewall")
        web_server = Server("Web Server")
        mail_server = Server("Mail Server")

    with Cluster("Core Network"):
        core_switch = Switch("Core Switch")
        
        with Cluster("Application Tier"):
            app_server1 = Server("App Server 1")
            app_server2 = Server("App Server 2")

        with Cluster("Database Tier"):
            db = Postgresql("PostgreSQL DB")

        with Cluster("Storage"):
            storage = Storage("NAS Storage")

        with Cluster("Monitoring"):
            monitoring = Custom("Zabbix", "./icons/zabbix.png")

    # Connections
    internet >> edge_fw >> edge_router >> dmz_fw
    dmz_fw >> web_server
    dmz_fw >> mail_server
    edge_router >> core_switch
    core_switch >> app_server1
    core_switch >> app_server2
    app_server1 >> db
    app_server2 >> db
    db >> storage
    core_switch >> monitoring
