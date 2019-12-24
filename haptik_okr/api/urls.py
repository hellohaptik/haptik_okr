from api.views import ForgotPasswordView, ResetForgottonPasswordView
from django.conf.urls import url
from django.urls import include

from api.views import LoginView, SignupView
from api.okr_views.views_homescreen import get_all_or_current_quarter, get_quarter_by_id, get_team_list_for_quarter_id
from api.okr_views.views_sheet import SheetView, SheetDetailView
from api.okr_views.views_objective import ObjectiveView, ObjectiveDetailView
from api.okr_views.views_keyresults import KeyResultsView, KeyResultsDetailsView

home_screen_urls = [
    url(r'^quarter/(?P<quarter_id>[0-9]+)/$', get_quarter_by_id),
    url(r'^quarter/$', get_all_or_current_quarter),
    url(r'^teams_progress/(?P<quarter_id>[0-9]+)/$', get_team_list_for_quarter_id),
]

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^signup/', SignupView.as_view(), name="signup"),
    url(r'^forgotpassword/', ForgotPasswordView.as_view(), name="forgotpassword"),
    url(r'^resetpassword/', ResetForgottonPasswordView.as_view(), name="resetforgottonpassword"),
    url('home/', include(home_screen_urls)),
    url(r'^sheet/$', SheetView.as_view(), name="sheet"),
    url(r'^sheet/(?P<sheet_id>[0-9]+)/$', SheetDetailView.as_view(), name="sheet_details"),
    url(r'^objective/$', ObjectiveView.as_view(), name="objective"),
    url(r'^objective/(?P<objective_id>[0-9]+)/$', ObjectiveDetailView.as_view(), name="objective_details"),
    url(r'^keyresult/$', KeyResultsView.as_view(), name="keyresults"),
    url(r'^keyresult/(?P<keyresult_id>[0-9]+)/$', KeyResultsDetailsView.as_view(), name="keyresults_details"),
]
