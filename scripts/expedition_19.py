from urllib.parse import urlparse, parse_qs
import sys
def parse_url(url):
    u = urlparse(url)
    return {"scheme": u.scheme, "host": u.netloc, "path": u.path, "query": parse_qs(u.query)}
if __name__ == "__main__":
    print(parse_url(sys.argv[1]))
