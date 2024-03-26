from django.urls import path, include
from work_flow.views import WorkFlowView, WorkFlowItemView

urlpatterns = [
    path('', WorkFlowView.as_view()),
    path("item/", WorkFlowItemView.as_view())
]