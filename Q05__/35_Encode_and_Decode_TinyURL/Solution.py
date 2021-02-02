import hashlib

class Codec:
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.library = {}        
        shortUrl = hashlib.md5(longUrl.encode()).hexdigest()
        self.library[ shortUrl ] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.library[ shortUrl ]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))