def is_leap(year):
  leap = False
  if year<1900:
      return leap
      pass
  elif year>=1900:

    # Write your logic here
    if year % 4 == 0:
        if (year / 4) % 2 == 0 or (year / 400) % 2 == 0:
            leap = True
        elif (year / 100) % 2 == 0:
            leap = False

    return leap


year = int(input())
print(is_leap(year))