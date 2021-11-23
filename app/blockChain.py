import hashlib
import json
from time import time
import re

from app.db_exception import *

class blockChain:
    
    def __init__(self, name = "") -> None:
        self.chain = []
        self.data = []
        self.name = name
        self.new_block(previous_hash=1)


    def __str__(self):
        return str(self.name)
    
    def valid_chain(self) -> bool:
        last_block = self.chain[0]
        current_index = 1
        while current_index < len(self.chain):
            block = self.chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False
            last_block = block
            current_index += 1
        return True

    def new_block(self, previous_hash=0):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.data,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.data = []
        self.chain.append(block)
        return block



    def new_data(self, nData) -> int:
        self.data.append(nData)
        return self.last_block['index'] + 1
    
    
    def revoke(self):

        if len(self.chain) <= 1:
            print("Empty chain")
            return False
        del self.chain[-1]
        return True   
    
    def printAll(self) -> str:
        pri = ""
        for i in self.chain:
            pri += str(i) + "\n"
        pri += str(self.valid_chain())
        return str(["" + str(i) for i in self.chain]) + str(self.valid_chain())

    def find(self, sah_str) -> str:
        count = 0
        pri = ""
        if sah_str == '*':
            for i in self.chain:
                pri += str(i) + '\n'
                count += 1
        else:
            for i in self.chain:
                if(re.search(sah_str, str(i['data']))):
                    pri += str(i) + "\n"
                    count += 1
        return "find " + str(count) + " msg:\n" + pri

    def spFind(self, sah_str) -> str:
        count = 0
        pri = ""
        if sah_str == '*':
            for i in self.chain:
                pri += str(i['data']) + '\n'
                count += 1
        else:
            for i in self.chain:
                if(re.search(sah_str, str(i['data']))):
                    pri += str(i['data']) + "\n"
                    count += 1
        return "find " + str(count) + " msg:\n" + pri
        
        
        
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
