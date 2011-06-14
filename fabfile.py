from fabric.api import local

def start():
    local("git pull origin master")
    
def prepare_deploy():
    # Tests here :)
    local("git add . && git commit")
