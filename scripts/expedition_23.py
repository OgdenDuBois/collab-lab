import sys
from datetime import datetime, timezone
def time_ago(ts):
    delta = datetime.now(timezone.utc) - datetime.fromtimestamp(int(ts), timezone.utc)
    secs = int(delta.total_seconds())
    if secs < 60:
        return f"{secs}s ago"
    if secs < 3600:
        return f"{secs // 60}m ago"
    if secs < 86400:
        return f"{secs // 3600}h ago"
    return f"{secs // 86400}d ago"
if __name__ == "__main__":
    print(time_ago(sys.argv[1]))
