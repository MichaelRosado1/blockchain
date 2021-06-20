'''
blockchain -> a digital ledger in which transactions made in cryptocurrency are recorded
chronologically and publicly

essentially a public database
'''
import hashlib 
import datetime as date 
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        #each block will have information on the index as well as the 
        #timestamp
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        #sha256 encryption used in crypto
        shaEncryption = hashlib.sha256()
        #hash the blocks attributes
        shaEncryption.update(str(self.index) + 
                             str(self.timestamp) + 
                             str(self.data) + 
                             str(self.previous_hash))
        #return this hash
        return shaEncryption


    

