#!/usr/bin/python3
# -*- coding: utf-8 -*-

# modules
import requests
import json
import logging
from datetime import datetime
import sys

# vars
baseUrl = "https://api.beget.com/api"
dateCurrentEpoch = datetime.today().timestamp()

begetAccountUser = sys.argv[1]
begetAccountPass = sys.argv[2]
domainIdFromShell = sys.argv[3]

try:
    # request session init
    responseSessionInit = requests.get(baseUrl +
                                       '/domain/getList?login=' + begetAccountUser + '&passwd=' + begetAccountPass + '&output_format=json')

# pass if error
except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)
    pass

# sessionJson(dict). pycharm 2018 x32 python 3.4
sessionJson = responseSessionInit.json()

# debug
#print(type(sessionJson).__name__)
#print(sessionJson)

# get list of services
domainsList = sessionJson['answer']['result']

# debug
#print(type(list).__name__)
#print(domainsList)

# for each service in list
for x in range(len(domainsList)):

    # get dict of services
    domainsDict = domainsList[x]

    # define vars
    domainId = domainsDict['id']
    domainExpirationDate = domainsDict['date_expire']

    # calc domain time left
    if (str(domainId) == domainIdFromShell):
        domainExpirationDateEpoch = datetime.strptime(domainExpirationDate, "%Y-%m-%d").timestamp()
        domainTimeLeft = (domainExpirationDateEpoch - dateCurrentEpoch)

        # output domain time epoch left
        print(domainTimeLeft)
