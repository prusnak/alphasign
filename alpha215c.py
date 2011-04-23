#!/usr/bin/python

import serial

class Alpha215C:

    def __init__(self, port = '/dev/ttyUSB0'):
        self.ser = serial.Serial(port = port, baudrate = 9600, bytesize = serial.SEVENBITS, parity = serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE)

    # modes from http://wls.wwco.com/ledsigns/alpha/protocol.html

    def send(self, mode, string):
        self.ser.write(25 * '\x00')
        self.ser.write('\x01Z00\x02AA\x1B ' + mode + string + '\x04')

    def clear(self):
        self.send('@', '')

    def scroll_left(self, string):
        self.send('a', string)

    def show(self, string):
        self.send('b', string)

    def flash(self, string):
        self.send('c', string)

    def random(self, string):
        self.send('d', string)
        # does 'o' the same?

    def scroll_up(self, string):
        self.send('e', string)
        # does 'm' the same?

    def scroll_down(self, string):
        self.send('f', string)

    def jerky_scroll_left(self, string):
        self.send('g', string)

    def jerky_scroll_right(self, string):
        self.send('h', string)

    def wipe_up(self, string):
        self.send('i', string)

    def wipe_down(self, string):
        self.send('j', string)

    def wipe_left(self, string):
        self.send('k', string)

    def wipe_right(self, string):
        self.send('l', string)

    def squish_in(self, string):
        self.send('p', string)
        # does 'x' the same?

    def push_out(self, string):
        self.send('q', string)
        # does 'y' the same?

    def cover(self, string):
        self.send('r', string)
        # does 'z' the same?

    def uncover(self, string):
        self.send('s', string)

    def compress(self, string):
        self.send('t', string)

    def fast(self, string):
        self.send('u', string)

    def medium(self, string):
        self.send('v', string)

    def slow(self, string):
        self.send('w', string)
