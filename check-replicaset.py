#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


# create mongodb client to connect primary node.
conn = ['localhost:27091']
c = MongoClient(conn)

# check replica set configuration
conf = c.admin.command('replSetGetConfig')
if conf['ok'] != 1.0:
    print('error, something wrong in replica set.')
    sys.exti(1)
else:
    print('replica set configration is ...')
    for m in conf['config']['members']:
        print('node: %s, priority: %s, votes: %s, tag: %s'
                % (m['host'], m['priority'], m['votes'], m['tags']))


# check replica set status
stat = c.admin.command('replSetGetStatus')
if stat['ok'] != 1.0:
    print('error, something wrong in replica set.')
    sys.exti(1)
else:
    print('replica set status is ...')
    for m in stat['members']:
        print('node: %s, role: %s'
                % (m['name'], m['stateStr']))

