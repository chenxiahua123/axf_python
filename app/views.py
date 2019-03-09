import hashlib
import random
from time import time

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Lunbo, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User


def base(request):
    # typenames = Foodtypes.objects.values('typename').distinct()
    #
    # data={
    #     'typenames':typenames
    # }

    return render(request,'base/base.html')


def home(request):

    lunbo=Lunbo.objects.all()

    nav=Nav.objects.all()

    mustbuys=Mustbuy.objects.all()

    shops=Shop.objects.all()

    mainshows=Mainshow.objects.all()

    data={
        'lunbos':lunbo,
        'navs':nav,
        'mustbuys':mustbuys,
        'shop0':shops[0],
        'shop1': shops[1:3],
        'shop2': shops[3:7],
        'shop3': shops[7:11],
        'mainshows':mainshows,
    }

    return render(request,'home/home.html',context=data)


def market(request,childid='0',sortid='0'):

    foodtypes=Foodtypes.objects.all()

    typenames=Foodtypes.objects.values('typename').distinct()



    # 默认打开是热销榜
    # 点击左侧分类，显示对应商品信息，传参categoryid

    index=int(request.COOKIES.get('index'))

    categoryid=foodtypes[index].typeid

    if childid=='0':
        goods = Goods.objects.filter(categoryid=categoryid)
    else:
        goods=Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    if sortid=='0':
        goods=goods.order_by('-productnum')
    elif sortid=='1':
        goods=goods.order_by('productnum')
    elif sortid=='2':
        goods = goods.order_by('-price')
    elif sortid =='3':
        goods = goods.order_by('price')

    childnames=foodtypes[index].childtypenames
    print(childid)

    child_list=[]
    for item in childnames.split('#'):
        items=item.split(':')
        temp_dir={
            'name':items[0],
            'id':items[1]
        }
        child_list.append(temp_dir)

    # typelist=[]
    #
    # for foodtype in foodtypes:
    #     list.append(foodtype.typename)
    #
    # typelist=set(list)
    #
    # print(typelist)
    #

    data={
        'foodtypes':foodtypes,
        'typenames':typenames,
        'goods':goods[0:30],
        'child_lists':child_list,
        'childid':childid,
    }


    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):

    token=request.session.get('token')

    userid=cache.get(token)

    if userid:
        user=User.objects.get(pk=userid)

        data={
            'user':user,
            'token':token,
        }
        return render(request,'mine/mine.html',context=data)
    else:
        return render(request,'mine/mine.html')







def genaret_password(param):
    md5=hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():

    token=str(time())+str(random.random)
    md5=hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()




def register(request):

    if request.method=='GET':
        return render(request, 'mine/register.html')
    elif request.method=='POST':

        user=User()
        user.username=request.POST.get('username')
        user.password=genaret_password(request.POST.get('password'))
        user.name=request.POST.get('name')

        user.save()

        token=generate_token()

        cache.set(token,user.id,60*60*24*3)

        request.session['token']=token

        return redirect('app:mine')


def logout(request):
    request.session.flush()
    return redirect('app:mine')


def login(request):

     if request.method=='GET':
         return render(request, 'mine/login.html')
     if request.method=='POST':

         username=request.POST.get('username')

         password=genaret_password(request.POST.get('password'))

         user=User.objects.filter(username=username).filter(password=password)

         if user:

             user=user.first()
             token=generate_token()

             cache.set(token,user.id)

             request.session['token']=token

             return redirect('app:mine')
         else:
            data={
                'error':'账户信息有误'
            }
            return render(request,'mine/login.html',context=data)






def check_01(request):

    username=request.GET.get('username')
    # print(username)
    user=User.objects.filter(username=username)
    #
    if user:
        return JsonResponse({'msg': '注册邮箱已被注册','status':0})
    else:
        return JsonResponse({'msg': '注册邮箱可使用', 'status':1})



