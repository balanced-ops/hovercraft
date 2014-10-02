from __future__ import unicode_literals


class Client(object):
    
    def __init__(self, docker_client):
        self.docker_client = docker_client

    def push(self, tag_or_id, name, version):
        """Push a local docker image to hovercraft. The tag_or_id is the tag
        name or image id for local docker image.

        """
