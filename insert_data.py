#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
from pymongo import MongoClient


# create mongodb client to connect primary node.
# set read preferece and replica set tags.
hosts = [
    'mongo-primary1:27017',
    'mongo-secondary1:27017',
    'mongo-secondary2:27017',
    'mongo-secondary3:27017',
    'mongo-secondary4:27017']

def random_data():
    return {
            "name": "".join(random.choices(string.ascii_lowercase, k=4)),
            "age": random.randint(20,50)}

try:
    c = MongoClient(host=hosts,
                    replicaSet='rs0',
                    readPreference='secondary',
                    readPreferenceTags='group:batch')
    db = c.test
    test = db.test

    # insert one
    test.insert_one({"name": "hoge", "age": 20})

    # insert many records
    doc = [ random_data() for n in range(1000)]
    test.insert_many(doc)

    c.close()
except Exception as e:
    print(type(e))
    print(e)
