def main():
    clock = input("What times is it? ").strip()
    clock = convert(clock)
    if 7  <= clock  <= 8:
        print("Breakfast Time")
    elif 12 <= clock <= 13:
        print("Lunch Time")
    elif 18 <= clock <= 19:
        print("Dinner Time")
def convert(time):
    is_am = " a.m." in time
    is_pm = " p.m." in time
    time = time.replace(":", "").replace(" a.m.", "").replace(" p.m.", "")
    if len(time) == 3:
        hours = int(time[:1])
        minutes = int(time[1:3])
    elif len(time) == 4:
        hours = int(time[:2])
        minutes = int(time[2:4])
    if is_pm and hours != 12:
        hours += 12
    if is_am and hours == 12:
        hours = 0

    print(float(hours + minutes/60))
    return float(hours + minutes/60)

if __name__ == "__main__":
    main()








