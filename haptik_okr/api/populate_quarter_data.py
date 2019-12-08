import datetime
from api.models.okr_related import Quarter, Sheet
from api.models.user_related import Team
from django.contrib.auth.models import User


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


def populate_team_data():
    teams = ['Mobile Team', 'Platform NextGen', 'Platform Enterprise', 'Marketing', 'Machine Learning']
    user = User.objects.last()
    for team in teams:
        Team.objects.create(name=team, head=user)


def populate_sheet_data():
    quarter = Quarter.objects.filter(is_current="True")[0]
    teams = Team.objects.all()
    for team in teams:
        Sheet.objects.create(team_id=team, quarter_id=quarter, progress=0)
