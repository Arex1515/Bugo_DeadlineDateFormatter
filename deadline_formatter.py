import datetime

event_title = input("Enter event title: ").strip()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime.date(year, month, day)
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", month_name, str(day) + ",", year)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday_name)
