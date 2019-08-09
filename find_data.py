#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient


# create mongodb client to connect primary node.
# set read preferece and replica set tags.
hosts = [
    'mongo-primary1:27017',
    'mongo-secondary1:27017',
    'mongo-secondary2:27017',
    'mongo-secondary3:27017',
    'mongo-secondary4:27017']
c = MongoClient(host=hosts, replicaSet='rs0', readPreference='secondary', readPreferenceTags='group:batch')

# connect test db, test collection
db = c.test
test = db.test

# check current connection preference
print(c)
print(c.server_info)
print(test.read_preference)

# select all document from test collection
for doc in test.find():
    print(doc)

c.close()
