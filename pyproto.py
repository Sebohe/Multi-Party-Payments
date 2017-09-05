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

local_web3 = Web3(HTTPProvider(os.environ['NODE']))

for k, account in enumerate(local_web3.eth.accounts):
        print ("{}: {}".format(k, account))

print ('Select account: ', end='')

accountSelected = int(input())

balance = local_web3.eth.getBalance(local_web3.eth.accounts[accountSelected])

print(local_web3.fromWei(balance, 'ether'))

account = local_web3.eth.accounts[accountSelected]

print ('Password:',end='')
local_web3.personal.unlockAccount(account, input())



myContract = local_web3.eth.contract()
myContract.abi = ABI
myContract.bytecode = BYTECODE
output = myContract.deploy()
print(output)
