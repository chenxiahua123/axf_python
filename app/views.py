from django.shortcuts import render

# Create your views here.
from app.models import Lunbo, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


def base(request):
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


def market(request):

    foodtypes=Foodtypes.objects.all()

    typenames=Foodtypes.objects.values('typename').distinct()

    goods=Goods.objects.all()
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
    }


    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')