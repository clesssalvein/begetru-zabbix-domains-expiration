#!/usr/bin/python3
# -*- coding: utf-8 -*-

# modules
import requests
import json
import logging
import sys

# vars
baseUrl = "https://api.beget.com/api"
begetAccountUser = sys.argv[1]
begetAccountPass = sys.argv[2]

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

# null string list of services
domainsListJsonForZabbix = ""

# add str data to str json
domainsListJsonForZabbix = (domainsListJsonForZabbix + "{\"data\":[")

# for each service in list
for x in range(len(domainsList)):

    # get dict of services
    domainsDict = domainsList[x]

    # debug
    #print(type(serviceDict).__name__)

    # define vars
    domainName = domainsDict['fqdn']
    domainId = domainsDict['id']

    # debug
    #print(serviceName + ' ' + serviceType + ' ' + str(serviceId))

    # construct json for zabbix
    domainsListJsonForZabbix = (
                domainsListJsonForZabbix + "{\"{#DOMAINNAME}\"" + ":" + "\"" + domainName + "\"" + ","
                + "\"{#DOMAINID}\"" + ":" + "\"" + str(domainId) + "\"" + "}")

    # add coma if not final service in list
    if not x == len(domainsList) - 1:
        domainsListJsonForZabbix = (domainsListJsonForZabbix + ",")

# add final round bracket to json for zabbix
domainsListJsonForZabbix = (domainsListJsonForZabbix + "]}")

# print json of services for zabbix to output
print(domainsListJsonForZabbix)
