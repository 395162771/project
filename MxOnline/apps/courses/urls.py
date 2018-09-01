from django.conf.urls import url
from .views import CourseListView, CourseDetailView ,CourseInfoView

urlpatterns = [
    # 公开课列表页
    url('^list/$', CourseListView.as_view(), name='course_list'),

    url('^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),


    url('^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

]
