time_in_seconds = int(raw_input("Enter time interval in seconds: "))
hours = time_in_seconds / 3600
minutes = (time_in_seconds - hours * 3600) / 60
seconds = time_in_seconds - (minutes * 60 + hours * 3600)

print ("%s seconds are equivalent to " % time_in_seconds)
print ("%15s:%s:%s" % (hours, minutes, seconds))
