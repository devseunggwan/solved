from datetime import datetime, timedelta

now = datetime.strptime(input(), "%B %d, %Y %H:%M")

new_year = datetime.strptime(str(now.year), "%Y")
end_year = datetime.strptime(str(now.year+1), "%Y")

past_year = now - new_year
full_yaer = end_year - new_year

print(past_year / full_yaer * 100)
