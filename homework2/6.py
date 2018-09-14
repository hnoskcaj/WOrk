t = float(input('Temperature in Fahrenheit '))
v = float(input('Speed in MPH '))
wc = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
print("It feels like " + str(wc))
