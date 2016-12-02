#!/usr/bin/env python

c.Jdk7Installer.user_dir = "/tmp"
c.Jdk7Installer.private_key = "/root/.ssh/id_rsa"
c.Jdk7Installer.ansible_exec = "ansible-playbook"
c.Jdk7Installer.ansible_host = ""
c.Jdk7Installer.ansible_playbook = "/home/liupengcheng/workspace/github/webpy/web/ansible/jdk.yaml" # set your own local playbook path
c.Jdk7Installer.ansible_envvars = {"package_path" : "/home/liupengcheng/Downloads/jdk1.7.0_55.tar.gz", # path to local jdk package
                                   "version" : "1.7.0_55",  # jdk version
                                   "jce_package_path" : "/home/liupengcheng/Downloads/jce_policy-7.zip",
                                   "user_dir" : "test_webpy"} # temp user dir name

