#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-07-03 10:28
brief:远程连接服务器，并发送命令
"""

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.5.176', port=22, username='holo', password=" ")

stdin, stdout, stderr = ssh.exec_command("ls /home/holo")
print stdout.read()

ssh.close()