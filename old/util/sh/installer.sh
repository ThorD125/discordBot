#!/bin/bash

apt install traceroute dnsutils -y
pip install -r requirements.txt

sudo cp /home/ther/discordBot/discord-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
