import random
import string

class URLShortener:
    def __init__(self, base_url = 'https://short/', short_length = 8):
        
        self.code_long_url: dict[str, str] = {}
        self.base_url = base_url
        self.short_length = short_length
    
    def _code_generator(self): # internal function thus '_'
        chars = string.ascii_letters + string.digits
        
        return ''.join(random.choice(chars) for _ in range(self.short_length))

    def shorten_url(self, long_url):
        
        key_comb = self._code_generator()
        
        while key_comb in self.code_long_url: # circumvents consistency
            key_comb = self._code_generator()
        
        self.code_long_url[key_comb] = long_url
        
        return self.base_url + key_comb
    
    def retrieve_long_url(self, shortened_url):
        
        # retrieve key from shortened url
        key = shortened_url.replace(self.base_url, '')
        
        return self.code_long_url.get(key) # assumes key exists 