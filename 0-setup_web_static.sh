#!/usr/bin/env bash
# Sets up web servers for deployment of web static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
IDX='/data/web_static/releases/test/index.html'
sudo echo -e "<!DOCTYPE html><body><p>Hello World</p>
</body></html>" | sudo tee $IDX
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
STR='location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'
sudo sed -i "38i $STR" /etc/nginx/sites-available/default
sudo service nginx restart
