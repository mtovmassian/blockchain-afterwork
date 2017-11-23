from block import Block

LIGTH_MAGENTA  = '\033[95m'
DEFAULT = '\033[m'

class Blockchain:

    def __init__(self):
        self.current_block = None
        self.add_genesis_block()

    def add(self, data):
        new_block = Block(data=data)
        self.current_block.next_block = new_block
        new_block.previous_block = self.current_block
        self.current_block = new_block

    def add_genesis_block(self):
        self.current_block = Block('I am the genesis block.')

    def get_current_block(self):
        return LIGTH_MAGENTA + "\n{0}\n".format(self.current_block) + DEFAULT

    def go_through(self):
        current_block = self.current_block
        while current_block is not None:
            input('[ENTER] to see previous block ')
            print(LIGTH_MAGENTA + "{0}".format(current_block) + DEFAULT)
            current_block = current_block.previous_block

    def __str__(self):
        current_block = self.current_block
        string = ""
        while current_block is not None:
            string = "\n{0}".format(current_block) if string == "" else "{0}\n{1}\n{1}\n{2}".format(
                string, '|'.center(100, ' '), current_block
            )
            current_block = current_block.previous_block
        return LIGTH_MAGENTA + string + '\n' + DEFAULT

if __name__ == '__main__':
    bc = Blockchain()
    bc.add('alpha block')
    bc.add('bravo block')
    bc.add('charly block')

    print(bc.get_current_block())
