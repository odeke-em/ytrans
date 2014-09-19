#!/usr/bin/env python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

import threading

import mp.JobRunner

class CacheConnector:
    def __init__(self, kvConnector=None):
        self.__entrails = kvConnector or {}
        self.__rlock = threading.RLock()
        self.__jobRunner = mp.JobRunner.JobRunner()

    def __getitem__(self, key, alt):
        return self.__entrails.get(key, alt)

    def get(self, key, alt=None):
        # Getting reads does not need to look the table, stale reads alright
        return self.__getitem__(key, alt)

    def __setitem__(self, key, value):
        return self.__entrails.__setitem__(key, value)

    def put(self, key, value, callback=None):
        return self.__jobRunner.run(
            self.__setitem__, self.__rlock, callback, key, value
        )

    def __pop(self, key, alt=None):
        return self.__entrails.pop(key, alt)


    def pop(self, key, alt=None, callback=None):
        return self.__jobRunner.run(
            self.__pop, self.__rlock, callback, key, alt
        )
