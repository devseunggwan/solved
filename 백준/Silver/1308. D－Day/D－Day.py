import datetime

times = [datetime.date(*map(int, input().strip().split())) for _ in range(2)]
period = times[1] - times[0]
period_over_1000year = datetime.date(times[0].year + 1000, times[0].month, times[0].day) - datetime.date(times[0].year, times[0].month, times[0].day)
print(f"D-{period.days}" if period.days < period_over_1000year.days else "gg")