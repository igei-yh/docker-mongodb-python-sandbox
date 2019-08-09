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


db = c.test
test = db.test

# insert one
test.insert_one(
    {
        "name": "hoge",
        "age": 20
    })

# insert many records
test.insert_many(
    [
        {"name": "fuga", "age": 30},
        {"name": "puge", "age": 40}
    ]
)

c.close()
