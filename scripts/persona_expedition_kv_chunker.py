"""Long-context KV chunker - ExpeditionEstates style.
Inspired by RedKnot: long-context LLM serving with KV reuse.
Split a long text into chunks, hash each chunk, reuse the
cached KV entry for repeated chunks and report the hit rate.
Usage: python persona_expedition_kv_chunker.py "long text here" 200
"""
import hashlib, sys

def chunk_text(text, size=200):
    return [text[i:i+size] for i in range(0, len(text), size)]

def kv_key(chunk):
    return hashlib.sha256(chunk.encode()).hexdigest()[:12]

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "hello world " * 50
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    cache, hits = {}, 0
    for i, chunk in enumerate(chunk_text(text, size)):
        key = kv_key(chunk)
        if key in cache:
            hits += 1
            print(f"chunk {i}: KV HIT  {key} (reused)")
        else:
            cache[key] = chunk
            print(f"chunk {i}: KV MISS {key} (cached)")
    total = len(chunk_text(text, size))
    print(f"chunks={total} cached={len(cache)} hits={hits} hit_rate={hits/total:.0%}")

if __name__ == "__main__":
    main()
