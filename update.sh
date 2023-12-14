#!/bin/bash

sudo systemctl stop discord-bot
git pull
sudo systemctl start discord-bot


