from datetime import datetime

date = datetime.now()
now = date.timestamp()

print(f"Seconds since January 1, 1970: {now:,.4f} or {format(now, '.2e')} in scientific notation")
print (date.strftime("%b %d %Y"))