from hashlib import sha256
from datetime import datetime


class Block():

    def __init__(self, data: str, prev_block_hash: str):
        self.time_stamp = str(datetime.now())
        self.data = data
        self.prev_block_hash = prev_block_hash
        self.hash_ = self.get_hash()

    def get_hash(self, prev_hash=None):
        if not prev_hash:
            prev_hash = self.prev_block_hash
        hasher = sha256()
        hasher.update(bytes(self.data + self.time_stamp + prev_hash,
                            'utf-8'))
        return hasher.hexdigest()

    def is_valid(self):
        return self.get_hash() == self.hash_

    def __str__(self):
        return f'---BlockStart---\n\
Data: {self.data}, \nTimeStamp: {self.time_stamp}, \n\
Hash: {self.hash_}, \nPreviousBlockHash: \
{self.prev_block_hash}\n---BlockEnd---'


class Chain():

    def __init__(self):
        genesis_block = Block('Genesis Block', '')
        self.chain = list()
        self.chain.append(genesis_block)

    def add_block(self, data: str):
        block = Block(data, self.chain[-1].hash_)
        self.chain.append(block)

    def is_valid(self):
        for block in self.chain:
            if self.chain.index(block) == 0:
                continue
            if block.get_hash(self.chain[
                    self.chain.index(block) - 1].hash_) == block.hash_:
                pass
            else:
                return False
        return True

    def __str__(self):
        return '\n\n'.join([str(block) for block in self.chain])

    # TODO set difficulty level.
