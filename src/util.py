import datetime

"""Generates date range skipping by @intervalDate"""
def daterange(startDate, endDate, skipDate=1):
    for n in range(int ((endDate - startDate).days) + skipDate):
        yield startDate + datetime.timedelta(n)