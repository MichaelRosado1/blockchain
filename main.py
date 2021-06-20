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
        shaEncryption.update(str(self.index).encode('utf-8') + 
                             str(self.timestamp) + 
                             str(self.data) + 
                             str(self.previous_hash))
        #return this hash
        return shaEncryption

#first block in the chain
def createGenesisBlock():
    #manually construct block
    return Block(0, date.datetime.now(), 'Genesis Block', '0')

def nextBlock(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = 'I am block ' + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def main():
    #intialize list to one block
    blockchain = [createGenesisBlock()] 
    previousBlock = blockchain[0]

    #number of blocks we want to create
    blockChainSize = 10

    for i in range(0, blockChainSize):
        newBlock = nextBlock(previousBlock)
        blockchain.append(newBlock)
        previousBlock = newBlock
        print "Block #{} has been added".format(newBlock.index)
        print "Hash: {}\n".format(newBlock.hash) 

if __name__ == '__main__':
    main()