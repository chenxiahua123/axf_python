from django.db import models

# Create your models here.
class Lunbo(models.Model):
    # img,name,trackid
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=100)

    class Meta:
        db_table='axf_wheel'

class Nav(models.Model):
    # img, name, trackid
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=100)

    class Meta:
        db_table='axf_nav'

class Mustbuy(models.Model):
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=100)

    class Meta:
        db_table='axf_mustbuy'

class Shop(models.Model):
    img=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=100)

    class Meta:
        db_table='axf_shop'

class Mainshow(models.Model):
    # trackid, name, img, categoryid, brandname, \
    # img1, childcid1, productid1, longname1, price1, marketprice1, \
    # img2, childcid2, productid2, longname2, price2, marketprice2, \
    # img3, childcid3, productid3, longname3, price3, marketprice3
    trackid=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    img= models.CharField(max_length=100)
    categoryid= models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)

    img1= models.CharField(max_length=100)
    childcid1= models.CharField(max_length=100)
    productid1= models.CharField(max_length=100)
    longname1= models.CharField(max_length=100)
    price1= models.CharField(max_length=100)
    marketprice1= models.CharField(max_length=100)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=100)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    marketprice2 = models.CharField(max_length=100)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=100)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    marketprice3 = models.CharField(max_length=100)

    class Meta:
        db_table='axf_mainshow'


class Foodtypes(models.Model):
    # typeid, typename, childtypenames, typesort
    typeid=models.CharField(max_length=100)
    typename=models.CharField(max_length=100)
    childtypenames=models.CharField(max_length=300)
    typesort=models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'

class Goods(models.Model):
    # productid, productimg, productname, productlongname,
    # isxf, pmdesc, specifics, price, marketprice,
    # categoryid, childcid,
    # childcidname, dealerid, storenums, productnum

    productid=models.CharField(max_length=100)
    productimg=models.CharField(max_length=300)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=200)
    isxf=models.IntegerField(default=0)
    pmdesc=models.IntegerField(default=0)
    specifics=models.CharField(max_length=100)

    price=models.DecimalField(max_digits=8,decimal_places=2)

    marketprice=models.DecimalField(max_digits=8,decimal_places=2)

    categoryid=models.IntegerField()

    childcid=models.IntegerField()

    childcidname=models.CharField(max_length=100)

    dealerid=models.CharField(max_length=100)

    storenums=models.IntegerField()

    productnum=models.IntegerField()

    class Meta:
        db_table='axf_goods'

class User(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=300)
    name=models.CharField(max_length=100)

    class Meta:
        db_table='注册用户信息'