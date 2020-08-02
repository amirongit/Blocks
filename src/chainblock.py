from hashlib import sha256
from datetime import datetime


class Block():

    def __init__(self, data: str, prev_block_hash: str):
        self.time_stamp = str(datetime.now())
        self.data = data
        self.hash_ = self.get_hash()

    def get_hash(self):
        hasher = sha256()
        hasher.update(bytes(self.data + self.time_stamp, 'utf-8'))
        return hasher.hexdigest()

    def is_valid(self):
        return self.get_hash() == self.hash_

    def __str__(self):
        return f'Data: {self.data}, \nTimeStamp: {self.time_stamp}, \n\
Hash: {self.hash_}\n---EndOfBlock---'


class Chain():

    def __init__(self):
        genesis_block = Block('Genesis Block', '')
        self.chain = list()
        self.chain.append(genesis_block)

    def add_block(self, data: str):
        block = Block(data, self.chain[-1].hash_)
        self.chain.append(block)

    # TODO set difficulty level.
