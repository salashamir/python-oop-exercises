"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Creates SerialGenerator with start value"""
        self.start = self.next = start

    def __repr__(self):
        """Representation of serial"""
        return f'<SerialGenerator start={self.start} next={self.initial}>'

    def generate(self):
        """Increments the value of the SerialGenerator by 1"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the value of the serialgenerator back to the initial start value"""
        self.next = self.start


