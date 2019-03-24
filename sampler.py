import shelve

class Sampler():

    def __init__(self, filename):
        self.filename = filename
        self.dict = shelve.open(self.filename)

    def makeKey(self, number):
        return str(round(number, 3))
    
    def sample(self, rpm_sum):
        exists = self.makeKey(rpm_sum) in self.dict
        
        return exists
        
    def lookup(self, rpm_sum):
        return self.dict[self.makeKey(rpm_sum)]
    
    def test(self):
        dict['key'] = 123.0
        dict['key2'] = 124.0
        
        data = dict['key']              # retrieve a COPY of data at key (raise KeyError if no such key)
                                   
        for key in dict.keys():
            print('%s: %s' % (key, dict[key]))
            
        del dict['key']                 # delete data stored at key (raises KeyError if no such key)
        
        
        dict.close()                  # close it
        return data