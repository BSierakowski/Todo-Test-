from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.key_filename = ['/home/brian/Downloads/briankp.pem']
env.user = 'ec2-user'
env.hosts = ['cibah.com']


def start():
    local("git pull origin master")
    
def prepare_deploy():
    # Tests here :)
    local("git add . && git commit")
    local("git push origin master")
      
def reboot():
    "Reboot httpd"
    sudo("httpd -k restart")
   
def stophttpd():
    "Stopping HTTPD"
    run("sudo httpd -k stop")
    
def starthttpd():
    "Starting HTTPD"
    run("sudo httpd -k start")
   
def pull():
    run("cd /var/www/app/; git pull origin master")   
