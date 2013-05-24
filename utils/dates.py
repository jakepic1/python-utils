from datetime import date, timedelta

AVG_DAYS_PER_YEAR = 365.2425

def timedelta_to_years(delta):
    """Convert a given timedelta to years (somewhat estimated)."""
    return delta.days / AVG_DAYS_PER_YEAR

def years_since_date(from_date):
    """Given a Date object, returns a float number of years
    since that date."""
    delta = date.today() - from_date
    return timedelta_to_years(delta)

def yeardelta(years):
    """Return a date exactly *years* years ago."""
    days = AVG_DAYS_PER_YEAR * years
    return timedelta(days=days)
