import datetime as dt

past_date = dt.datetime(1970, 1, 1)
now = dt.datetime.now()

diff_sec = now - past_date
diff_sec = diff_sec.total_seconds()

print(f"Seconds since January 1, 1970: {float(diff_sec):,.4f} or {float(diff_sec):.2e} in scientific notation")
print(f"{dt.datetime.now().strftime('%b %d %Y')}")