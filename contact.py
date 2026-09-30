class Contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.city = zip

    def __lt__(self, other):
        self.other = other
        if other[0][1] == other[1][1]:
            return other[0][0] > other[1][0]
        else:
            return other[0][1] > other[1][1]


    def __str__(self):
        return self

    def __rept__(self):
        return self