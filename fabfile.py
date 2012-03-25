from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'michael_he@sanjose.dreamhost.com'
DEST_PATH = '/home/michael_he/hezhigeng.com/newblog'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

hydecmd = '../hyde1.0/h'

def clean():
    local('rm -rf ./deploy')

def gen():
    local('python '+ hydecmd + ' -v gen')

def regen():
    clean()
    gen()

def serve():
    local('python '+ hydecmd + ' -w -s . -k -p 8081')

def reserve():
    regen()
    serve()

def smush():
    local('smusher ./media/images')

@hosts(PROD)
def publish():
    # regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
