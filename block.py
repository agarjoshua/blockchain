import time

from crypto_hash crypto_hash
GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'data': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:


    def __init__(self,timestamp,last_hash,hash,data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
    
    def __repr__(self):
        return (
            'Block('
            f'timestamp:{self.timestamp},'
            f'last_hash:{self.last_hash},'
            f'hash:{self.hash},'
            f'data:{self.data},'
            f'difficulty:{self.difficulty},'

        )

    @staticmethod
    def mine_block(last_block, data):

        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp,last_hash,hash, data)

        return Block(timestamp, last_hash, hash, data)


    @staticmethod
    def genesis():


        return Block(1, 'genesis_last_hash', 'genesis_hash', [])

