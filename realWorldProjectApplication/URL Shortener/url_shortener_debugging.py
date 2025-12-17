import random
import string

class URLShortener:
    def __init__(self, base_url="https://sho.rt/"):
        self.base_url = base_url # mark as internal use only
        self.code_to_url = {}

    def _generate_code(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def shorten(self, long_url):
        code = self._generate_code() # to reduce collision and code space, perhaps using hashlib and base64 (just a representation) will be more efficient
        # collision check needed to avoid accidental rewrites
        self.code_to_url[code] = long_url
        return self.base_url + code

    def resolve(self, short_url):
        code = short_url.split("/")[-1]
        # need to implement gracefully handling keyError
        return self.code_to_url[code]