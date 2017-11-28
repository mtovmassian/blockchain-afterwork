import datetime
import hashlib

SHA = hashlib.sha256()
GREEN  = '\033[1;32m'
BLACK = '\033[1;30m'
DEFAULT = '\033[m'

class Block:

    def __init__(self, data):
        self.__data = data
        self.timestamp = datetime.datetime.now()
        self.hash = self.gen_hash()
        self.block_index = None
        self.previous_block_hash = None
        self.next_block_hash = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data
        self.timestamp = datetime.datetime.now()
        self.hash = self.gen_hash()

    def gen_hash(self):
        return (lambda x=SHA.update(str({self.timestamp, self.__data}).encode()): SHA.hexdigest())()

    def __str__(self):
        width = 100
        long_edge = GREEN + "{0}".format('/' * width) + DEFAULT
        short_edge = GREEN + '//' + DEFAULT
        row = lambda attr, val: short_edge + BLACK + "    {0}: {1}".format(attr, val).ljust(width-4, ' ') + short_edge

        block_index = row(attr='block_index', val=self.block_index)
        hash = row(attr='hash', val=self.hash)
        timestamp = row(attr='timestamp', val=self.timestamp)
        previous_block_hash = row(attr='previous_block_hash', val=None if self.previous_block_hash == None else self.previous_block_hash)
        next_block_hash = row(attr='next_block_hash', val=None if self.next_block_hash == None else self.next_block_hash)
        data = row(attr='data', val=self.data)

        return "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}".format(
            long_edge, block_index, hash, timestamp, previous_block_hash, next_block_hash, data, long_edge
        ) + DEFAULT

if __name__ == '__main__':
    b = Block('alpha block')
    print(b)
    b.data = 'michel'
    print(b)
