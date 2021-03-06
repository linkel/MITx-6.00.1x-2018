class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Returns a set of integers that both sets share"""
        newList = intSet()
        for integers in self.vals:
            if integers in other.vals:
                newList.insert(integers)
        return newList

    def __len__(self):
        """Returns the length of the integer set"""
        return len(self.vals)

hi = intSet()
hi.insert(3)
hi.insert(4)
hi.insert(5)
bye = intSet()
bye.insert(2)
newy = hi.intersect(bye)
print(newy)
print(len(hi))
print(len(newy))