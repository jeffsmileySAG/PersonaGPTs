# from py_d2.D2Diagram import D2Diagram, D2Node, D2Relation
from py_d2 import D2Diagram, D2Shape, D2Connection, D2Style, D2Relation, D2Node, D2Diagram


# Initialize the diagram
diagram = D2Diagram()

# Home Private Network (Internal Services)
private_network1 = D2Node("private_network1", label="Home Private Network (Internal Services)")
ms_a1 = D2Node("ms_a1", label="MINISFORUM MS-A1 Ryzen 7 Mini-PC NAS")
beelink_ser6 = D2Node("beelink_ser6", label="Beelink SER6 Ryzen 7 Mini-PC Internal Services")
unraid = D2Node("unraid", label="Unraid")
nginx_proxy = D2Node("nginx_proxy", label="Nginx Proxy Manager")
dokuwiki = D2Node("dokuwiki", label="DokuWiki")
immich = D2Node("immich", label="Immich")
homer = D2Node("homer", label="Homer Dashboard")
calibre = D2Node("calibre", label="Calibre Web")
freshrss = D2Node("freshrss", label="FreshRSS")
jellyfin = D2Node("jellyfin", label="Jellyfin")

# Add nodes to the diagram for Home Private Network
diagram.add_node(private_network1)
diagram.add_node(ms_a1)
diagram.add_node(beelink_ser6)
diagram.add_node(unraid)
diagram.add_node(nginx_proxy)
diagram.add_node(dokuwiki)
diagram.add_node(immich)
diagram.add_node(homer)
diagram.add_node(calibre)
diagram.add_node(freshrss)
diagram.add_node(jellyfin)

# Create relationships for Home Private Network
diagram.add_relation(D2Relation(ms_a1, unraid, "Unraid"))
diagram.add_relation(D2Relation(beelink_ser6, nginx_proxy))
diagram.add_relation(D2Relation(beelink_ser6, dokuwiki))
diagram.add_relation(D2Relation(beelink_ser6, immich))
diagram.add_relation(D2Relation(beelink_ser6, homer))
diagram.add_relation(D2Relation(beelink_ser6, calibre))
diagram.add_relation(D2Relation(beelink_ser6, freshrss))
diagram.add_relation(D2Relation(beelink_ser6, jellyfin))

# IoT and Guest Network
iot_network = D2Node("iot_network", label="Internet-of-Things & Guest Network")
asus_ap = D2Node("asus_ap", label="ASUS AC68-P 2.4-5GHz IoT AP MerlinWRT")
philips_hub = D2Node("philips_hub", label="Phillips Hue Bridge Zigbee")
iot_clients = D2Node("iot_clients", label="Wireless Clients IoT Devices")

# Add nodes to the diagram for IoT Network
diagram.add_node(iot_network)
diagram.add_node(asus_ap)
diagram.add_node(philips_hub)
diagram.add_node(iot_clients)

# Create relationships for IoT Network
diagram.add_relation(D2Relation(asus_ap, philips_hub))
diagram.add_relation(D2Relation(asus_ap, iot_clients))

# Publicly Accessible Web Services (External Services)
web_services = D2Node("web_services", label="Publicly Accessible Web Services")
minisforum_um690 = D2Node("minisforum_um690", label="MINISFORUM UM690S Ryzen 9 Mini-PC External Services")
nginx_proxy_web = D2Node("nginx_proxy_web", label="Nginx Proxy Manager")
seafile = D2Node("seafile", label="Seafile")
gotosocial = D2Node("gotosocial", label="GoToSocial")
linkstack = D2Node("linkstack", label="LinkStack")
ollama = D2Node("ollama", label="Ollama LLM OpenWebUI")
pro_website = D2Node("pro_website", label="Professional Website")
personal_website = D2Node("personal_website", label="Personal Website")
nifty = D2Node("nifty", label="Nifty")
uptime_kuma = D2Node("uptime_kuma", label="Uptime Kuma")

# Add nodes to the diagram for Web Services
diagram.add_node(web_services)
diagram.add_node(minisforum_um690)
diagram.add_node(nginx_proxy_web)
diagram.add_node(seafile)
diagram.add_node(gotosocial)
diagram.add_node(linkstack)
diagram.add_node(ollama)
diagram.add_node(pro_website)
diagram.add_node(personal_website)
diagram.add_node(nifty)
diagram.add_node(uptime_kuma)

# Create relationships for Web Services
diagram.add_relation(D2Relation(minisforum_um690, nginx_proxy_web))
diagram.add_relation(D2Relation(minisforum_um690, seafile))
diagram.add_relation(D2Relation(minisforum_um690, gotosocial))
diagram.add_relation(D2Relation(minisforum_um690, linkstack))
diagram.add_relation(D2Relation(minisforum_um690, ollama))
diagram.add_relation(D2Relation(minisforum_um690, pro_website))
diagram.add_relation(D2Relation(minisforum_um690, personal_website))
diagram.add_relation(D2Relation(minisforum_um690, nifty))
diagram.add_relation(D2Relation(minisforum_um690, uptime_kuma))

# Main Network Infrastructure
main_network = D2Node("main_network", label="Main Network Infrastructure")
isp_wan = D2Node("isp_wan", label="ISP Fiber WAN")
pfsense = D2Node("pfsense", label="Protectli VP2420 4x 2.5G Port PfSense Firewall + Router")
cloudflare = D2Node("cloudflare", label="Cloudflare Reverse DNS")

# Add nodes to the diagram for Main Network
diagram.add_node(main_network)
diagram.add_node(isp_wan)
diagram.add_node(pfsense)
diagram.add_node(cloudflare)

# Create relationships for Main Network Infrastructure
diagram.add_relation(D2Relation(isp_wan, pfsense, "Exposed ports: HTTP-HTTPS, Wireguard"))
diagram.add_relation(D2Relation(pfsense, cloudflare))

# Additional Network Connections
remote_clients = D2Node("remote_clients", label="Remote Clients Wireguard")
ubiquiti_switch = D2Node("ubiquiti_switch", label="Ubiquiti Flex-Mini 4x 2.5G Port")
tp_link = D2Node("tp_link", label="TP-Link TL-PoE260S 1x 2.5GbE PoE+ Injector")
ubiquiti_ap = D2Node("ubiquiti_ap", label="Ubiquiti U7 Pro WiFi 7 AP")
internal_clients = D2Node("internal_clients", label="Wireless Clients Internal")

# Add nodes for additional connections
diagram.add_node(remote_clients)
diagram.add_node(ubiquiti_switch)
diagram.add_node(tp_link)
diagram.add_node(ubiquiti_ap)
diagram.add_node(internal_clients)

# Create additional network relationships
diagram.add_relation(D2Relation(cloudflare, remote_clients))
diagram.add_relation(D2Relation(pfsense, ubiquiti_switch))
diagram.add_relation(D2Relation(ubiquiti_switch, private_network1))
diagram.add_relation(D2Relation(ubiquiti_switch, iot_network))
diagram.add_relation(D2Relation(ubiquiti_switch, web_services))
diagram.add_relation(D2Relation(ubiquiti_switch, tp_link))
diagram.add_relation(D2Relation(tp_link, ubiquiti_ap))
diagram.add_relation(D2Relation(ubiquiti_ap, internal_clients))

# Generate and print D2 code
d2_code = diagram.generate_d2_code()
print(d2_code)
