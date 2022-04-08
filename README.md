# Hetzner-Cloud-Firewall-Cloudflare-Updater
A Python script that automatically updates a Hetzner Cloud firewall to accept HTTP(s) traffic from Cloudflare only

Installation:
```bash
git clone https://github.com/JeffResc/Hetzner-Cloud-Firewall-Cloudflare-Updater
cd Hetzner-Cloud-Firewall-Cloudflare-Updater
python3 -m venv Hetzner-Cloud-Firewall-Cloudflare-Updater
source Hetzner-Cloud-Firewall-Cloudflare-Updater/bin/activate
pip3 install -r requirements.txt
```

Usage:
```bash
python3 updater.py <API_TOKEN> <Hetzner_Firewall_ID>
```
