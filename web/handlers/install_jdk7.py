#!/usr/bin/env python
from __future__ import print_function
from handler import Handler
import os
import subprocess


def format_env_args(kwargs):
  if not type(kwargs) is dict:
    raise TypeError("kwargs not dict type.")
  buildargs = []
  for k, v in kwargs.iteritems():
    buildargs.append("-e")
    buildargs.append("%s=%s" % (k, v))
  return buildargs


def start_host_name(name, path):
  print("[%s]" % name, file=path)


def append_host(host_ip, path):
  print(host_ip, file=path)


def write_host_file(host):
  host_file = os.path.join(Jdk7Installer.user_dir, "install_jdk7.host")
  f = open(host_file, 'w')
  try:
    start_host_name("all", f)
    if isinstance(host, tuple):
      for h in host:
        append_host(h, f)
    else:
      append_host(host, f)
  finally:
    f.close()
  return host_file

def get_or_create_hostfile(host):
	if not host:
		return Jdk7Installer.ansible_host
	else:
		return write_host_file(host)

name = "Jdk7Installer"


class Jdk7Installer(Handler):
  user_dir = ""
  private_key = ""
  ansible_exec = ""
  ansible_host = ""
  ansible_playbook = ""
  ansible_envvars = {}

  def handle(self, *host, **kwargs):
    if not Jdk7Installer.private_key:
      raise Exception("private_key is not set")
    print(host)
    print(kwargs)
    Jdk7Installer.ansible_host = get_or_create_hostfile(host)
    cmd = [Jdk7Installer.ansible_exec,  
					"-i", Jdk7Installer.ansible_host, 
           Jdk7Installer.ansible_playbook,  
				   "--private-key", Jdk7Installer.private_key, 
					 ] + format_env_args(
      Jdk7Installer.ansible_envvars)
    print("ansible command: " + " ".join(cmd))
    os.environ["ANSIBLE_HOST_KEY_CHECKING"] = "False"
    child = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    err_msg = self.read_stderr(child.stderr)
    if child.wait() != 0:
      raise Exception("ansible execution error:%s" % err_msg)
    else:
      return "successful"

  def read_stderr(self, stderr):
    return stderr.read()
