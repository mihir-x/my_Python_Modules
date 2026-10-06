from datetime import date

birth = input("Enter your Birthday (YYYY-MM-DD): ")
year, month, day = map(int, birth.split("-"))

birthday = date(year, month, day)
today = date.today()

age = today.year - birthday.year - ((today.month,today.day)<(birthday.month,birthday.day))

print(f"You are {age} years old")
