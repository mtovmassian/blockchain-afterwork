from block import Block

GREEN  = '\033[1;32m'
BLACK = '\033[1;30m'
DEFAULT = '\033[m'

class Blockchain:

    def __init__(self):
        self.current_block = None
        self.chain = []
        self.genesis_block = None
        self.add_genesis_block()

    def add(self, data):
        new_block = Block(data=data)
        new_block.block_index = self.current_block.block_index + 1
        self.current_block.next_block_hash = new_block.hash
        new_block.previous_block_hash = self.current_block.hash
        self.chain.append(new_block)
        self.current_block = new_block

    def add_genesis_block(self):
        self.genesis_block = Block('I am the genesis block.')
        self.current_block = self.genesis_block
        self.current_block.block_index = 0
        self.chain.append(self.current_block)

    def get_current_block(self):
        return GREEN + "\n{0}\n".format(self.current_block) + DEFAULT

    def search(self, block_hash):
        block = None
        try:
            block = next(block for block in self.chain if block.hash == block_hash)
        except StopIteration:
            print("/!\ No block found.")
        return block

    def navigate_up(self):
        current_block = self.genesis_block
        print(GREEN + "{0}".format(current_block) + DEFAULT)
        while current_block.next_block_hash is not None:
            try:
                input("\nONE BLOCK UP [PRESS ENTER]\n")
                current_block = next(block for block in self.chain if block.hash == current_block.next_block_hash)
                print(GREEN + "{0}".format(current_block) + DEFAULT)
            except StopIteration:
                self.throw_corruption_error(current_block, "after")
                break

    def navigate_down(self):
        current_block = self.current_block
        print(GREEN + "{0}".format(current_block) + DEFAULT)
        while current_block.previous_block_hash is not None:
            try:
                input("\nONE BLOCK DOWN [PRESS ENTER]\n")
                current_block = next(block for block in self.chain if block.hash == current_block.previous_block_hash)
                print(GREEN + "{0}".format(current_block) + DEFAULT)
            except StopIteration:
                self.throw_corruption_error(current_block, "before")
                break

    def throw_corruption_error(self, block, position):
        alert = "/!\ BLOCKCHAIN CORRUPTION HAS BEEN DETECTED /!\\"
        info = "\nCan't retrieve blocks {0} block {1}\n".format(position, block.block_index)
        error = alert + info
        print(error)

    def __str__(self):
        current_block = self.current_block
        string = "\n{0}".format(current_block)
        while current_block.previous_block_hash is not None:
            try:
                current_block = next(block for block in self.chain if block.hash == current_block.previous_block_hash)
                string = "{0}\n{1}\n{1}\n{2}".format(string, GREEN + '|'.center(100, ' ') + DEFAULT, current_block)
            except StopIteration:
                self.throw_corruption_error(current_block, "before")
        return string + '\n'


if __name__ == '__main__':
    bc = Blockchain()
    bc.add('alpha block')
    bc.add('bravo block')

    print(bc)
