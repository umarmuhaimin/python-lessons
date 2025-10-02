def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        print(f"Moisture is {moisture}%")

    print("It's time to water")

main()

# 🔹 Target of this project:

# → To monitor soil moisture levels.
# → To keep checking moisture until it is low enough (20% or less).
# → To notify you when it’s time to water the soil.

# 👉 Calls a function called sample() to get the current moisture level.
# → Prints the moisture level as a percentage.
# → While the moisture is above 20%, keeps checking the moisture by calling sample() again and printing the new value.
# → When the moisture drops to 20% or below, prints "It's time to water" and stops.

#########################################################################################################################

def main():
    moisture = sample()
    days = 0
    print(f"Day {days} : Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Moisture is {moisture}%")

    print("It's time to water")

main()

# 👉 The addition of days variable is to track how many days have passed while checking the moisture.
# → days += 1 is to increase the day count starting from day = 0 to present day.

# 🔹 Summary of the changes:
# → We add a day counter.
# → Prints the day and moisture level at the start.
# → Intended to update the day count each time the loop runs.