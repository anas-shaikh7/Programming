months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
def main():
    formatted_date = dates("Date: ")
    print(formatted_date)



def dates(date1):
    while True:
        try: # month/day/year OR  month day, year
            date = input(date1)
            if "/" in date:
                month, day, year = date.split("/")
                m = int(month)
                d = int(day)
                y = int(year)
                if 0 < m <= 12 and 0 < d <= 31 and 0 < y <= 2026:
                    return f"{y}-{m:02}-{d:02}"

            elif ...:
                for i in range(len(months)):
                    if months[i] in date:
                        m_n_d1, y1 = date.split(", ")
                        m1, d1 = m_n_d1.split(" ")
                        m1 = i + 1
                        d1 = int(d1)
                        y1 = int(y1)
                        if 0 < m1 <= 12 and 0 < d1 <= 31 and 0 < y1 <= 2026:
                            return f"{y1}-{m1:02}-{d1:02}"
        except ValueError:
            pass

main()