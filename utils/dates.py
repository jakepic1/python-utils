import datetime

def years_from_date_to_date(from_date, to_date):
    from_month, from_day, from_year = from_date
    to_month, to_day, to_year = to_date
    year_diff = to_year - from_year
    if from_month > to_month or ((from_month == to_month) and (from_day == to_day)):
        return year_diff - float((from_month - to_month))/12
    return year_diff + float((to_month - from_month))/12

def years_since_date(month, day, year):
    today = datetime.date.today()
    return years_from_date_to_date(
        (month, day, year,),
        (today.month, today.day, today.year,))
