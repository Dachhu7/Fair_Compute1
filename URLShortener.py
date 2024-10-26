import hashlib

class URLShortener:
    def __init__(self):
        # Dictionary to store short and long URL pairs
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Generate a hash for the long URL
        short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]  # Shortened to 6 characters
        short_url = f"http://short.ly/{short_hash}"
        
        # Map the short URL to the original long URL
        self.url_mapping[short_url] = long_url
        return short_url

    def retrieve_url(self, short_url):
        # Retrieve the original URL from the short URL
        return self.url_mapping.get(short_url, "URL not found")

# Example usage
shortener = URLShortener()
long_url = "https://www.example.com/this-is-a-very-long-url-for-testing-purposes"
short_url = shortener.shorten_url(long_url)

print("Original URL:", long_url)
print("Shortened URL:", short_url)

# Retrieve the original URL
retrieved_url = shortener.retrieve_url(short_url)
print("Retrieved URL:", retrieved_url)
