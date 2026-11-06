def daily_calories(weight_kg, height_cm, age, active=True):
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    factor = 1.55 if active else 1.2
    return bmr * factor

if __name__ == "__main__":
    cals = daily_calories(70, 175, 30)
    print(f"Daily calories: {cals:.0f} kcal")
    print(f"Light day: {daily_calories(70, 175, 30, False):.0f} kcal")
