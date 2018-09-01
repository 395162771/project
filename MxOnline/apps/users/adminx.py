__date__ = '2018/8/16 19:34'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):  # app 全局配置
    enable_themes = True  # 主题功能
    use_bootswatch = True


class GlobleSetting(object):
    # 固定参数 需要记住
    site_title = 'Spider在线教学后台管理系统'
    site_footer = 'Spider 在线教学网'

    # 后台左侧数据创建可下拉菜单
    menu_style = 'accordion'


class EmailVerifyRecordAadmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    search_fields = ('code', 'email', 'send_type')
    list_filter = ('code', 'email', 'send_type', 'send_time')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'index', 'add_time')
    search_fields = ('title', 'image', 'url', 'index')
    list_filter = ('title', 'image', 'url', 'index', 'add_time')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAadmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobleSetting)
