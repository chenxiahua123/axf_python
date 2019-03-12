from django.conf.urls import url

from app import views

urlpatterns=[
    url(r'^base/$', views.base, name='base'),
    url(r'^home/$', views.home, name='home'),
    url(r'^market/$', views.market, name='marketbase'),
    url(r'^market/(?P<childid>\d+)/(?P<sortid>\d+)/$', views.market, name='market'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^mine/$', views.mine, name='mine'),

    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    # 检测注册——ajax
    url(r'^check_01/$', views.check_01, name='check_01'),
    url(r'^check_02/$', views.check_02, name='check_02'),
    url(r'^check_03/$', views.check_03, name='check_03'),
    # url(r'^check_04/$', views.check_04, name='check_04'),

    url(r'^addcart/$', views.addcart, name='addcart'),
    url(r'^minuscart/$', views.minuscart, name='minuscart'),
    url(r'^changestatus/$',views.changestatus,name='changestatus'),
    url(r'^changeall/$',views.changeall,name='changeall'),

    # 订单操作
    # 生成订单
    url(r'^generateorder/$', views.generateorder, name='generateorder'),
]