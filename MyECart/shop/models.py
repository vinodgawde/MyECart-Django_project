from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    product_desc=models.CharField(max_length=400)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70, default="")
    title=models.CharField(max_length=100, default="")
    msg=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    phone=models.CharField(max_length=100, default="")
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
