from datetime import datetime, timedelta

def bedtime(wake_time, hours=8):
    wake = datetime.strptime(wake_time, "%H:%M")
    return (wake - timedelta(hours=hours)).strftime("%H:%M")

def sleep_cycles(wake_time):
    return [bedtime(wake_time, h) for h in (6, 7.5, 9)]

if __name__ == "__main__":
    print(f"Wake 07:00, sleep by: {bedtime("07:00")}")
    print(f"Good bedtimes: {sleep_cycles("07:00")}")
