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
    def __init__(self, start=0):
        self.start = self.next = start
    def __repr__(self):
        """Creates unique incrementing serial numbers, start = self.start, next= self.next"""
        return f"<SerialGenerator start = {self.start} next={self.next}>"
    def generate_number(self):
        """generates next sequential number"""
        self.next += 1
        return self.next
    def reset_count(self):
        """resets the count to start"""
        self.next = self.start 


    
    