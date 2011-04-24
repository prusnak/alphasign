import serial

RED = '\x1C1'
GREEN = '\x1C2'
AMBER = '\x1C3'
DIMRED = '\x1C4'
DIMGREEN = '\x1C5'
BROWN = '\x1C6'
ORANGE = '\x1C7'
YELLOW = '\x1C8'
RAINBOW1 = '\x1C9'
RAINBOW2 = '\x1CA'
COLORMIX = '\x1CB'
AUTOCOLOR = '\x1CC'
BOLD = '\x1D01'
NOBOLD = '\x1D00'

class AlphaSign:

    def __init__(self, port = '/dev/ttyUSB0'):
        # defaults: 9600, 8bits, none parity, one stopbit
        self.ser = serial.Serial(port = port)

    def text(self, mode, string):
        s  = 5 * '\x00' # packet sync characters
        s += '\x01'     # start of header
        s += 'Z'        # all types
        s += '00'       # broadcast address
        s += '\x02'     # start of text
        s += 'A'        # text mode
        s += 'A'        # file label
        s += '\x1B'     # start of text
        s += ' '        # use middle line (irrelevant on singleline display)
        s += mode       # display mode
        s += '\x1C1'    # set default color = red
        s += string     # text to display
        s += '\x04'     # end of transmission
        self.ser.write(s)

    def clear(self):
        self.text('@', '')

    def rotate(self, string):
        self.text('a', string)

    def hold(self, string):
        self.text('b', string)

    def flash(self, string):
        self.text('c', string)

    def roll_up(self, string):
        self.text('e', string)

    def roll_down(self, string):
        self.text('f', string)

    def roll_left(self, string):
        self.text('g', string)

    def roll_right(self, string):
        self.text('h', string)

    def wipe_up(self, string):
        self.text('i', string)

    def wipe_down(self, string):
        self.text('j', string)

    def wipe_left(self, string):
        self.text('k', string)

    def wipe_right(self, string):
        self.text('l', string)

    def random(self, string):
        self.text('o', string)

    def roll_in(self, string):
        self.text('p', string)

    def roll_out(self, string):
        self.text('q', string)

    def wipe_in(self, string):
        self.text('r', string)

    def wipe_out(self, string):
        self.text('s', string)

    def compressed(self, string):
        self.text('t', string)

    def twinkle(self, string):
        self.text('n0', string)

    def sparkle(self, string):
        self.text('n1', string)

    def snow(self, string):
        self.text('n2', string)

    def interlock(self, string):
        self.text('n3', string)

    def switch(self, string):
        self.text('n4', string)

    def slide(self, string):
        self.text('n5', string)

    def spray(self, string):
        self.text('n6', string)

    def starburst(self, string):
        self.text('n7', string)

    def welcome(self, string = ''):
        self.text('n8', string)

    def slotmachine(self, string = ''):
        self.text('n9', '')

    def thankyou(self, string = ''):
        self.text('nS', string)

    def nosmoking(self, string = ''):
        self.text('nU', string)

    def drink(self, string = ''):
        self.text('nV', string)

    def animal(self, string = ''):
        self.text('nW', string)

    def fireworks(self, string = ''):
        self.text('nX', string)

    def turbocar(self, string = ''):
        self.text('nY', string)

    def bomb(self, string = ''):
        self.text('nZ', string)
