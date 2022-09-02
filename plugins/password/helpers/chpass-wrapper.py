#!/usr/bin/env python

import sys
import pwd
import subprocess

BLACKLIST = (
    # add blacklisted users here
    #'user1',
)

try:
    username, password = sys.stdin.readline().split(':', 1)
except ValueError:
    sys.exit('Malformed input')

try:
    user = pwd.getpwnam(username)
except KeyError:
    sys.exit(f'No such user: {username}')

if user.pw_uid < 1000:
    sys.exit('Changing the password for user id < 1000 is forbidden')

if username in BLACKLIST:
    sys.exit(
        f'Changing password for user {username} is forbidden (user blacklisted)'
    )


handle = subprocess.Popen('/usr/sbin/chpasswd', stdin = subprocess.PIPE, universal_newlines = True)
handle.communicate(f'{username}:{password}')

sys.exit(handle.returncode)
