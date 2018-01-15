#!/usr/bin/env python3

#This is an early prototype python web3 interface to learn how to deploy
#contracts. It defaults to the first account available.
#
#Make sure you have the NODE enviroment variable set to your not.
#In linux it would be like:
# $export NODE='http://localhost:8545'

from abi import ABI, BYTECODE
from web3 import Web3, HTTPProvider
import json
import os

"""
        os.environ['NODE'],
        'http://localhost:8545'
        ]
""" 

hosts = 

for address in hosts:
    print (address)

    try:
        w3 = Web3(HTTPProvider(address))
        print (w3.eth.blockNumber)
    except Exception as e:
        print(e)
        pass


print (w3.eth.accounts)


if len(w3.eth.accounts) == 1:
    accountSelected = 0
else:
    print ('Select account: ', end='')
    accountSelected = int(input())


balance = w3.eth.getBalance(w3.eth.accounts[accountSelected])

print(w3.fromWei(balance, 'ether'))
"""
account = local_web3.eth.accounts[accountSelected]

print ('Password:',end='')
local_web3.personal.unlockAccount(account, input())



myContract = local_web3.eth.contract()
myContract.abi = ABI
myContract.bytecode = BYTECODE
output = myContract.deploy()
print(output)

"""
