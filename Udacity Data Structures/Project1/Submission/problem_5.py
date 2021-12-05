import hashlib
import time
import datetime


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

    def __repr__(self):
        return "Block" + '\nTimestamp:' + str(time.strftime('%Y-%m-%dT%H:%M:%SZ', self.timestamp)) + '\nData:' + str(self.data) + '\nPrevious Hash:' + str(self.previous_hash) + '\n'


class BlockChain:
    def __init__(self, data=None):
        self.tail = Block(time.gmtime(time.time()), data, 0)

    def insert(self, data):
        new_block = Block(time.gmtime(time.time()), data, self.tail.hash)
        self.tail = new_block

    def __repr__(self):
        return str(self.tail)


# test statements
b1 = BlockChain()
# should print None because there is no block in b2 chain
print(b1.tail.data)

# all the timestamps are same because they are declared at same time (Hrs:Min)
b2 = BlockChain('here')
print(b2)
b2.insert("one")
print(b2.tail.timestamp)
b2.insert("two")
print(b2.tail.timestamp)
b2.insert("three")
print(b2.tail.timestamp)
print(b2)

b3 = BlockChain('data')
b3.insert('data1')
print(b3.tail.hash)
b3.insert('data2')
print(b3.tail.hash)
