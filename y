[Unit]
Description=Discord Bot Service
After=network.target

[Service]
ExecStart=/bin/bash /home/ther/discordBot/update.sh
Restart=always
RestartSec=3
User=ther
Group=ther

[Install]
WantedBy=multi-user.target

