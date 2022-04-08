import requests
import sys
from hcloud import Client
from hcloud.firewalls.domain import FirewallRule

def update_hetzner_firewall(subnets, token, firewall_id):
    # Create hcloud client
    client = Client(token=token)

    # Get the firewall
    firewall = client.firewalls.get_by_id(id=firewall_id)

    # Create firewall rules
    http_rule = FirewallRule(
        direction=FirewallRule.DIRECTION_IN,
        port='80',
        protocol=FirewallRule.PROTOCOL_TCP,
        source_ips=subnets,
        description='Allow HTTP traffic from Cloudflare'
    )
    https_rule = FirewallRule(
        direction=FirewallRule.DIRECTION_IN,
        port='443',
        protocol=FirewallRule.PROTOCOL_TCP,
        source_ips=subnets,
        description='Allow HTTPS traffic from Cloudflare'
    )

    # Sets firewall rules
    try:
        client.firewalls.set_rules(firewall=firewall, rules=[http_rule, https_rule])
        print('Firewall updated')
    except Exception as e:
        print('Error updating firewall: {}'.format(e))


def get_cloudflare_ips():
    # Get the list of Cloudflare IPs from their endpoint
    subnets = requests.get('https://www.cloudflare.com/ips-v4').content.decode().split('\n')
    ipv6_subnets = requests.get('https://www.cloudflare.com/ips-v6').content.decode().split('\n')

    # Add the two lists
    subnets.extend(ipv6_subnets)
    return subnets

if __name__ == "__main__":
    # Get the arguments
    try:
        token = sys.argv[1]
        firewall_id = sys.argv[2]
    except IndexError:
        print("Usage: python3 updater.py <API_TOKEN> <Hetzner_Firewall_ID>")
        sys.exit(1)

    # Get the Cloudflare IPs
    subnets = get_cloudflare_ips()

    # Update the firewall
    update_hetzner_firewall(subnets, token, firewall_id)

