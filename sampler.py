import shelve

class Sampler():

    def setup(self):
        self.dict = shelve.open(self.filename)

    def __init__(self, filename):
        self.filename = filename
        self.setup()

    def close(self):
        self.dict.close()
        
    def makeKey(self, number1, number2):
        return str(round(number1)) + str(round(number2))
    
    def sample(self, start_rpm, max_rpm):
        key = self.makeKey(start_rpm, max_rpm)
        exists = key in self.dict
        
        self.dict[key] = key
        
        return exists
        
    def lookup(self, rpm_sum):
        return self.dict[self.makeKey(rpm_sum)]
    
    # TODO #8 Remove when done with issue 
    def test(self):
        for key in self.dict.keys():
            print('%s: %s' % (key, self.dict[key]))
