from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.key_filename = ['/home/brian/Downloads/briankp.pem']
env.user = 'ec2-user'
env.hosts = ['cibah.com']

def pack():
    local('tar czf /tmp/todo.tgz .')  
  
def deploy():
    pack()
    put('/tmp/todo.tgz', '/tmp/')
    with cd('/var/www/app/'):
        run('sudo tar xzf /tmp/todo.tgz')
    run('cd /var/www/app/ && sudo rm fabfile.py && sudo rm fabfile.pyc')
    reboot()

def reboot():
    "Reboot httpd"
    run("sudo httpd -k restart")
   
def stophttpd():
    "Stopping HTTPD"
    run("sudo httpd -k stop")
    
def starthttpd():
    "Starting HTTPD"
    run("sudo httpd -k start")
   

