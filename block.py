import datetime
import hashlib

SHA = hashlib.sha256()

class Block:

    def __init__(self, data):
        self.timestamp = datetime.datetime.now()
        self.hash = (lambda x=(lambda: SHA.update(str(self.timestamp).encode()))(): SHA.hexdigest())()
        self.previous_block = None
        self.next_block = None
        self.data = data

    def __str__(self):
        width = 100
        sep_l, sep_h = '/', '//'
        block_edge = "{0}".format(sep_l * width)
        hash = "{0}    hash: {1}".format(sep_h, self.hash).ljust(width-2, ' ') + sep_h
        timestamp = "{0}    timestamp: {1}".format(sep_h, self.timestamp).ljust(width-2, ' ') + sep_h
        previous_block_hash = "{0}    previous_block: {1}".format(
            sep_h, None if self.previous_block == None else self.previous_block.hash).ljust(width-2, ' '
        ) + sep_h
        next_block_hash = "{0}    next_block: {1}".format(
            sep_h, None if self.next_block == None else self.next_block.hash).ljust(width-2, ' '
        ) + sep_h
        data = "{0}    data: {1}".format(sep_h, self.data).ljust(width-2, ' ') + sep_h

        return "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}".format(
            block_edge, hash, timestamp, previous_block_hash, next_block_hash, data, block_edge
        )
