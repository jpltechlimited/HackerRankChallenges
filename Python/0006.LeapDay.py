def is_evenly_divided(numerator, denominator):
    isEvenlyDivided = False
    if numerator % denominator == 0:
        isEvenlyDivided = True
    return isEvenlyDivided

def is_leap(year):
    leap = False
    if is_evenly_divided(year, 4):
        if is_evenly_divided(year, 100) & is_evenly_divided(year, 400):
            leap = True
        elif is_evenly_divided(year, 100):
            leap = False
        else:
            leap = True
    else:
        leap = False    
    return leap

years = [2000,2400,1800,1900, 2100, 2200, 2300, 2500, 1992]
for year in years:
    print (year , is_leap(year))