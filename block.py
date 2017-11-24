import datetime
import hashlib

SHA = hashlib.sha256()
LIGTH_MAGENTA  = '\033[95m'
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
        sep_l, sep_h = '/', '//'
        block_edge = "{0}".format(sep_l * width)
        block_index = "{0}    block_index: {1}".format(sep_h, self.block_index).ljust(width-2, ' ') + sep_h
        hash = "{0}    hash: {1}".format(sep_h, self.hash).ljust(width-2, ' ') + sep_h
        timestamp = "{0}    timestamp: {1}".format(sep_h, self.timestamp).ljust(width-2, ' ') + sep_h
        previous_block_hash = "{0}    previous_block_hash: {1}".format(
            sep_h, None if self.previous_block_hash == None else self.previous_block_hash).ljust(width-2, ' '
        ) + sep_h
        next_block_hash = "{0}    next_block_hash: {1}".format(
            sep_h, None if self.next_block_hash == None else self.next_block_hash).ljust(width-2, ' '
        ) + sep_h
        data = "{0}    data: {1}".format(sep_h, self.data).ljust(width-2, ' ') + sep_h

        return LIGTH_MAGENTA + "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}".format(
            block_edge, block_index, hash, timestamp, previous_block_hash, next_block_hash, data, block_edge
        ) + DEFAULT

if __name__ == '__main__':
    b = Block('alpha block')
    print(b)
    b.data = 'michel'
    print(b)
