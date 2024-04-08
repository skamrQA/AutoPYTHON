def is_year_leap(year):
    if year % 4 >= 1 :
        print("год ", year,":", False)
    elif year % 4 == 0 and year % 100 >= 1:
        print("год ", year, ":", True)
    elif year % 100 == 0 and year % 400 >= 1:
        print("год ", year, ":", False)
    elif year % 100 == 0 or year % 400 == 0:
        print("год ", year, ":", True)
    else:
        print("год ", year, ":", "FOFF")
is_year_leap(2000)