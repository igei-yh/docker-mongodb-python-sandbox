#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient


# define replica set config
config = {'_id': 'rs0', 'members':[
    {'_id': 0, 'host': 'mongo-primary1:27017', 'priority': 10, 'votes': 1, 'tags': {'group': 'web'} },
    {'_id': 1, 'host': 'mongo-secondary1:27017', 'priority': 1, 'votes': 1, 'tags': {'group': 'api'}},
    {'_id': 2, 'host': 'mongo-secondary2:27017', 'priority': 1, 'votes': 1, 'tags': {'group': 'web'}},
    {'_id': 3, 'host': 'mongo-secondary3:27017', 'priority': 0, 'votes': 0, 'tags': {'group': 'standby'}},
    {'_id': 4, 'host': 'mongo-secondary4:27017', 'priority': 0, 'votes': 0, 'tags': {'group': 'standby'}}]}

try:
    # create mongodb client to connect primary node.
    conn = ['mongo-primary1:27017']
    c = MongoClient(conn)

    # check primary connection,
    # and connect admin database and exec replicaset configure
    c.admin.command('replSetInitiate', config)
    c.close()
except Exception as e:
    print(type(e))
    print(e)
