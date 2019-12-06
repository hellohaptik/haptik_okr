from django.conf.urls import url
from django.urls import path, include

from api.views import LoginView, SignupView
from api.views_homescreen import get_all_or_current_quarter, get_quarter_by_id

home_screen_urls = [
    url(r'^quarter/(?P<quarter_id>[0-9]+)/$', get_quarter_by_id),
    url(r'^quarter/$', get_all_or_current_quarter),
]

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^signup/', SignupView.as_view(), name="signup"),
    url('home/', include(home_screen_urls))
]
