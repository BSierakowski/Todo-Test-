from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.key_filename = ['/home/brian/Downloads/briankp.pem']
env.user = ['ec2-user']
env.hosts = ['cibah.com']


def start():
    local("git pull origin master")
    
def prepare_deploy():
    # Tests here :)
    local("git add . && git commit")
    
def git_reset():
    "Resets the repository to specified version."
    run("cd /var/www/app/; git reset --hard $(hash)")
   
def reboot():
    "Reboot httpd"
    sudo("httpd -k restart")
   
def pull():
    run("cd /var/www/app/; git pull origin master")
        
def reset(repo, hash):
    """
    Reset all git repositories to specified hash.
    Usage:
        fab reset:repo=my_repo,hash=etcetc123
    """
    require("fab_hosts", provided_by=[production])
    config.hash = hash
    config.repo = repo
    invoke(git_reset)
    
