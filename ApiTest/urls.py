"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome),  # 获取菜单
    path('home/',views.home),  # 进入首页
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", views.child),  # 返回子页面
    path('login/',views.login),  # 进入登陆页面
    path('login_action/',views.login_action),  # 登陆
    path('register_action/',views.register_action), # 注册
    path('accounts/login/',views.login),  # 非登陆状态下自动跳回登陆页面
    path('logout/',views.logout),  # 退出登陆
    path('pei/',views.pei),  # 匿名吐槽
    path('help/',views.api_help),  # 进入到帮助文档
    path('project_list/',views.project_list),  # 进入项目列表
    path('delete_project/',views.delete_project),  # 删除项目
    path('add_project/',views.add_project),  # 新增项目
    re_path(r"^apis/(?P<id>.*)/$", views.open_apis),  # 进入接口库
    re_path(r"^cases/(?P<id>.*)/$", views.open_cases),  # 进入用例设置
    re_path(r"^project_set/(?P<id>.*)/$", views.open_project_set),  # 进入项目设置
    re_path(r"^save_project_set/(?P<id>.*)/$",views.save_project_set),  # 保存项目设置
    re_path(r"^project_api_add/(?P<Pid>.*)/$", views.project_api_add),  # 新增接口
    re_path(r"^project_api_del/(?P<id>.*)/$", views.project_api_del),  # 新增接口
    path('save_bz/',views.save_bz),  # 保存备注
    path('get_bz/',views.get_bz),  # 获取备注
    path('Api_save/',views.Api_save),  # 保存接口
    path('get_api_data/',views.get_api_data),  # 获取接口数据
    path('Api_send/',views.Api_send),  # 调试层发送请求
    path('copy_api/',views.copy_api),  # 复制接口
    path('error_request/',views.error_request),  # 调用异常测试接口
]
