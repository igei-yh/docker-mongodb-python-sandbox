#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

# create mongodb client to connect primary node.
conn = ['localhost:27091']
c = MongoClient(conn)

# get current replica set configuration
conf = c.admin.command('replSetGetConfig')

# check status of getting configuration
if conf['ok'] != 1.0:
    print('error, something wrong in replica set.')
    sys.exti(1)
else:
    # get reconfig to change configuration
    reconfig = conf['config']
    try:
        for m in conf['config']['members']:
            tag = m.get('tags')
            if tag['group'] == 'standby':
                reconfig['members'][m['_id']]['tags'] = {'group': 'web'}

        # new config version must be greater than old one
        reconfig['version']+=1

        # execute reconfig operaiton
        c.admin.command('replSetReconfig', reconfig)
    except Exception as e:
        print(type(e))
        print(e)
