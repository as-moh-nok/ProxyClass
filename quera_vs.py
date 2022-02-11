class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.calls = {}
        self.last_invoked = ""
        self.attrs = dir(self._obj)
        
    def __getattr__(self, method):
        if method in self.attrs:
            print("in Proxy to get")
            d = getattr(self._obj , method)
            d()
            self.last_invoked =str(method)
            if method in self.calls:
                self.calls[method] += 1
            else:
                self.calls[method] = 0
        else:
            print("Oops!no method like this!")
            raise Exception('No Method Is Invoked')
            
        self.last_invoked =str(method)
        self.calls[method] += 1
          
    
    #def __setattr__(self, value):
    #    pass

    def count_of_calls(self, method_name):
        try:
            return self.calls[method_name]
        except:
            return 0
        

    def was_called(self, method_name):
        if self.calls[method_name] != None:
            return True
        return False
 

   
class Radio():   
    def __init__(self):        
        self._channel = None        
        self.is_on = False        
        self.volume = 0        

    #def __getattribute__(self, method): #clean it!
    #    pass

    
    def get_channel(self): 
        print(self._channel)
        return self._channel    

    def set_channel(self, value):        
        self._channel = value        

    def power(self):        
        self.is_on = not self.is_on

print("Get start!")      
r = Radio()
r._channel = "kerman"
p = Proxy(r)
getattr(p,'get_channel')
#print(getattr(p,'get_channel'))
#print(p.call('s_channel'))
