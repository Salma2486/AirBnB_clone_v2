#!/usr/bin/env bash
#jskrtg dlkn esglknes rlkng
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ directory to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*location \/hbnb_static/ {s/^\s*#*\s*//;}' $config_file
sudo sed -i '/^\s*location \/hbnb_static/ {s/alias .*/alias \/data\/web_static\/current\/;/;}' $config_file
# Restart Nginx
sudo service nginx restart
