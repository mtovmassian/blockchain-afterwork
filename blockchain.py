from block import Block

LIGTH_MAGENTA  = '\033[95m'
DEFAULT = '\033[m'

class Blockchain:

    def __init__(self):
        self.current_block = None
        self.chain = []
        self.add_genesis_block()

    def add(self, data):
        new_block = Block(data=data)
        new_block.block_index = self.current_block.block_index + 1
        self.current_block.next_block_hash = new_block.hash
        new_block.previous_block_hash = self.current_block.hash
        self.chain.append(new_block)
        self.current_block = new_block

    def add_genesis_block(self):
        self.current_block = Block('I am the genesis block.')
        self.current_block.block_index = 0
        self.chain.append(self.current_block)

    def get_current_block(self):
        return LIGTH_MAGENTA + "\n{0}\n".format(self.current_block) + DEFAULT

    def search(self, block_index):
        block = None
        current_block = self.current_block
        try:
            block = next(block for block in self.chain if block.block_index == block_index)
        except StopIteration:
            print("/!\ No block found.")
        return block

    def go_down(self):
        current_block = self.current_block
        while current_block is not None:
            input('[PREVIOUS] ')
            print(LIGTH_MAGENTA + "{0}".format(current_block) + DEFAULT)
            current_block = current_block.previous_block

    def __str__(self):
        current_block = self.current_block
        string = "\n{0}".format(current_block)
        while current_block.previous_block_hash is not None:
            try:
                current_block = next(block for block in self.chain if block.hash == current_block.previous_block_hash)
                string = "{0}\n{1}\n{1}\n{2}".format(string, LIGTH_MAGENTA + '|'.center(100, ' '), current_block)
            except StopIteration:
                string = "\n{0}\nCant't retrieve blocks before block {1}.\n".format("/!\ Blockchain is corrupted.", current_block.block_index)
                break
        return LIGTH_MAGENTA + string + '\n' + DEFAULT


if __name__ == '__main__':
    bc = Blockchain()
    bc.add('alpha block')
    bc.add('bravo block')
    bc.add('charly block')
    bc.add('delta block')

    print(bc)
