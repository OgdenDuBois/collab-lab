import time

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...")
        time.sleep(1)
    print("Time is up!")

if __name__ == "__main__":
    print("Starting a 3 second countdown:")
    countdown(3)
