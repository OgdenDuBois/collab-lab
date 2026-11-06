def reading_time(word_count, wpm=200):
    return word_count / wpm

def format_time(minutes):
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    return f"{hours}h {mins}m" if hours else f"{mins}m"

if __name__ == "__main__":
    words = 12000
    print(f"{words} words take about {format_time(reading_time(words))}")
    print(f"500 words take about {format_time(reading_time(500))}")
