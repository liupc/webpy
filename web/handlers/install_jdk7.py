#!/usr/bin/env python
from handler import Handler
import subprocess

name = "Jdk7Installer"
class Jdk7Installer(Handler):
    jdk_download_url = ""
    private_key = ""
    ansible_exec = ""
    ansible_host = ""
    ansible_playbook = ""
    def handle(self, *args):
        if not jdk_download_url:
            raise Exception("jdk_download_url is not set")
        if not private_key:
            raise Exception("private_key is not set")
        cmd = (Jdk7Installer.ansible_exec, "-i", Jdk7Installer.ansible_host \
            Jdk7Installer.ansible_playbook)
        child = subprocess.Popen(cmd, stderr=subprocess.PIPE)
        err_msg = self.read_stderr(child.stderr)
        if child.wait() != 0:
            raise Exception("ansible execution error:%s" % err_msg)

    def read_stderr(self, stderr):
        return stderr.read()
