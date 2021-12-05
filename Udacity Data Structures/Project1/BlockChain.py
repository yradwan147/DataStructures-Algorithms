import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data, timestamp, previous_hash)

    def calc_hash(self, data, timestamp, previous_hash):
        sha = hashlib.sha256()

        hash_str = (str(timestamp)+"||"+str(data)+"||" +
                    str(previous_hash)).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self, data):
        self.tail = Block(time.gmtime(time.time()), data, 0)

    def insert(self, data):
        new_block = Block(time.gmtime(time.time()), data, self.tail.hash)
        self.tail = new_block
