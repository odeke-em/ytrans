#!/usr/bin/env python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

import re
import requests

import setup
import CacheConnector

reSpaceSubCompile = re.compile('\s+', re.UNICODE)

class YTrans:
    def fmtUrlAsJSON(text, format='text'):
        return '{tu}/api/{av}/{tr}'.format(
            tu=setup.TRANSLATE_URL, av=setup.API_VERSION, tr=setup.JSON_INTERFACE
        ), ''

    def fmtUrlAsXML(text, format='text'):
        return '{tu}/api/{av}/{tr}'.format(
            tu=setup.TRANSLATE_URL, av=setup.API_VERSION, tr=setup.XML_INTERFACE
        ), ''

    def fmtUrlAsJSONP(text, myCallbackUrl, format='text'):
        return '{tu}/api/{av}/{tr}'.format(
            tu=setup.TRANSLATE_URL, av=setup.API_VERSION, tr=setup.JSON_INTERFACE
        ), 'callback={cb}'.format(myCallbackUrl)


    def __init__(self, apiKey, **cacheConnkwargs):
        self.__apiKey = apiKey
        assert(self.__apiKey)

        self.__cache = CacheConnector.CacheConnector(**cacheConnkwargs)

    def __fmtUrlForTrans(self, content, outputEnum=setup.JSON_ENUM):
        orderIndexDict = {}
        outputStr = ''
        if isinstance(content, list) or isinstance(content, tuple):
            for i, l in enumerate(content):
                orderIndexDict[i] = l 
                outputStr += 'text=%s'%(reSpaceSubCompile.sub('+', str(l)))

    def getLangs(self):
        pass

    def detectLang(self):
        pass

    def translate(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
