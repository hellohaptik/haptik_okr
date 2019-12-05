import datetime
from api.models.okr_related import Quarter


def populate_quarter_data():
    years = [2018, 2019]
    quarter_dates_names = [(1, 3, 1, 31, "Q1"), (4, 6, 1, 30, "Q2"), (7, 9, 1, 30, "Q3"), (10, 12, 1, 31, "Q4")]

    for year in years:
        for quarter_detail in quarter_dates_names:
            Quarter.objects.create(quarter_name=quarter_detail[4],
                                   quarter_start_date=datetime.date(year, quarter_detail[0],
                                                                    quarter_detail[2]),
                                   quarter_end_date=datetime.date(year, quarter_detail[1],
                                                                  quarter_detail[3]),
                                   is_current=False)
