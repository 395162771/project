from organization.views import OrgView

__date__ = '2018/8/23 0023 上午 11:00'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFvaView

urlpatterns = [
    # 课程机构列表页
    url('^list/$', OrgView.as_view(), name='org_list'),
    url('add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url('home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url('course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url('desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url('teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    url('add_fav/$', AddFvaView.as_view(), name='add_fav'),

]
