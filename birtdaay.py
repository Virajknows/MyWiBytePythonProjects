import time
from datetime import datetime

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_DAY = 24 * 60 * 60


def ask_birthday():
    while True:
        try:
            year = int(input("Enter your birth year (e.g. 2010): "))
            month = int(input("Enter your birth month (1-12): "))
            day = int(input("Enter your birth day (1-31): "))
            birth_date = datetime(year, month, day)
        except ValueError:
            print("That is not a valid date. Please try again.\n")
            continue

        if birth_date > datetime.now():
            print("That date is in the future. Please try again.\n")
        else:
            return birth_date


def birthday_in_year(year, month, day):
    try:
        return datetime(year, month, day)
    except ValueError:
        return datetime(year, 3, 1)


def find_next_birthday(birth_date, now):
    this_year = birthday_in_year(now.year, birth_date.month, birth_date.day)
    if this_year > now:
        return this_year
    return birthday_in_year(now.year + 1, birth_date.month, birth_date.day)


def translate_time(total_seconds):
    days = total_seconds // SECONDS_PER_DAY
    hours = (total_seconds % SECONDS_PER_DAY) // SECONDS_PER_HOUR
    minutes = (total_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds = total_seconds % SECONDS_PER_MINUTE
    return days, hours, minutes, seconds


def seconds_left(next_birthday):
    return int((next_birthday - datetime.now()).total_seconds())


def countdown(next_birthday):
    try:
        remaining = seconds_left(next_birthday)
        while remaining > 0:
            days, hours, minutes, seconds = translate_time(remaining)
            message = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds left"
            print("\r" + message.ljust(60), end="", flush=True)
            time.sleep(1)
            remaining = seconds_left(next_birthday)
        print("\nHappy Birthday!")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")


def main():
    print("=== Birthday Countdown ===")
    birth_date = ask_birthday()
    now = datetime.now()

    weekday_name = WEEKDAYS[birth_date.weekday()]
    print(f"\nYou were born on a {weekday_name}.")

    if now.month == birth_date.month and now.day == birth_date.day:
        print("Today is your birthday - Happy Birthday!")

    next_birthday = find_next_birthday(birth_date, now)
    if next_birthday.year == now.year:
        when = "this year"
    else:
        when = "next year"

    next_weekday = WEEKDAYS[next_birthday.weekday()]
    age = next_birthday.year - birth_date.year
    print(f"Your next birthday is {when}, on {next_weekday} {next_birthday.strftime('%d %B %Y')}.")
    print(f"You will be turning {age}.")

    days, hours, minutes, seconds = translate_time(seconds_left(next_birthday))
    print(f"\nTime left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    print("\nStarting the countdown (press Ctrl+C to stop)...\n")
    countdown(next_birthday)


if __name__ == "__main__":
    main()
