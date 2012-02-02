from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'michael_he@sanjose.dreamhost.com'
DEST_PATH = '/home/michael_he/hezhigeng.com/newblog'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    local('rm -rf ./deploy')

def generate():
    local('python ../hyde/hyde.py -g -s .')

def regen():
    clean()
    generate()

def serve():
    local('python ../hyde/hyde.py -w -s . -k -p 8081')

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