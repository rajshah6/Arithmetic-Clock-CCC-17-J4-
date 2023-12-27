def getIntInput(prompt = "Enter an integer: ", exceptStatement = "Invalid input. "):
    while True:
        try:
            var = int(input(prompt))
            return var

        except ValueError:
            print(exceptStatement, end = "")

def timeConverter(addedMinutes):
    hours = addedMinutes // 60
    minutes = addedMinutes - hours*60
    hours %= 12

    if minutes < 10:
        minutes = f"0{minutes}"

    if hours == 0:
        hours = 12

    time = list(str(hours)) + list(str(minutes))
    time = [int(i) for i in time]

    return hours, minutes, time

# get input
addedMinutes = getIntInput("Enter minutes after 12:00: ")
while addedMinutes < 0:
    addedMinutes = getIntInput("Invalid input. Enter minutes after 12:00: ", "")

hours, minutes, time = timeConverter(addedMinutes)
print(f"Current Time: {hours}:{minutes}\n")

# display arithmetic times
arithmeticTimes = []

for min in range(addedMinutes+1 if addedMinutes <= 720 else 721):
    hours, minutes, time = timeConverter(min)

    for i in range(1, len(time)-1):
        if time[i] - time[i-1] != time[i+1] - time[i]:
            break
    else:
        arithmeticTimes.append(f"{hours}:{minutes}")

print(f"All Arithmetic Times: {', '.join(arithmeticTimes) if arithmeticTimes != [] else None}")
print(f"Total: {len(arithmeticTimes)}")
