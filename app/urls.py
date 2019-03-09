from django.conf.urls import url

from app import views

urlpatterns=[
    url(r'^base/$',views.base,name='base'),
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='marketbase'),
    url(r'^market/(?P<childid>\d+)/(?P<sortid>\d+)/$',views.market,name='market'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),

    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^login/$',views.login,name='login'),
    # 检测注册——ajax
    url(r'^check_01/$',views.check_01,name='check_01')
]