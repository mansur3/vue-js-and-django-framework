from django.urls import path
from team_member.views import TeamMemberView

urlpatterns = [
    path('', TeamMemberView.as_view())
]