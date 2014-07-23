Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com
* current setup on iguana is:

server {
    listen 80;
    server_name iguana.cs.toronto.edu;
	
    location /static {
	alias /home/mbrown/sites/iguana.cs.toronto.edu/static;	
	}
    location / {
	rewrite .* http://urbantrees.ca/treemap permanent;
    }
    location /treemap {
        proxy_pass http://localhost:8000/treemap;
    }
}

## Upstart Job
* install gunicorn using ../virtualenv/bin/pip3 install gunicorn==18
* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv