from django.db import models


from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ('-name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'listings:product_list_by_category',
            args=[self.slug]
        )

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'products',
        on_delete = models.CASCADE
    )

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    video = models.FileField(upload_to='products/')
    main_image = models.ImageField(upload_to='products/')
    image1=models.ImageField(upload_to='products/' ,null=True,blank=True)
    image2=models.ImageField(upload_to='products/' ,null=True,blank=True)
    image3=models.ImageField(upload_to='products/',null=True,blank=True)
    image4=models.ImageField(upload_to='products/',null=True,blank=True)
    image5=models.ImageField(upload_to='products/',null=True,blank=True)
    image6=models.ImageField(upload_to='products/',null=True,blank=True)
    color=models.BooleanField(default=True)
    color1=models.BooleanField(default=True)
    color2=models.BooleanField(default=True)
    color3=models.BooleanField(default=True)
    color4=models.BooleanField(default=True)
    color5=models.BooleanField(default=True)
    color6=models.BooleanField(default=True)
    color7=models.BooleanField(default=True)
    color8=models.BooleanField(default=True)
    color9=models.BooleanField(default=True)
    color10=models.BooleanField(default=True)
    color_1=models.CharField(max_length=50,null=True,blank=True)
    color_2=models.CharField(max_length=50,null=True,blank=True)
    color_3=models.CharField(max_length=50,null=True,blank=True)
    color_4=models.CharField(max_length=50,null=True,blank=True)
    color_5=models.CharField(max_length=50,null=True,blank=True)
    color_6=models.CharField(max_length=50,null=True,blank=True)
    color_7=models.CharField(max_length=50,null=True,blank=True)
    color_8=models.CharField(max_length=50,null=True,blank=True)
    color_9=models.CharField(max_length=50,null=True,blank=True)
    color_10=models.CharField(max_length=50,null=True,blank=True)
    size=models.BooleanField(default=False)
    size1=models.BooleanField(default=True)
    size2=models.BooleanField(default=True)
    size3=models.BooleanField(default=True)
    size4=models.BooleanField(default=True)
    size5=models.BooleanField(default=True)
    size6=models.BooleanField(default=True)
    size_1=models.CharField(max_length=200,null=True,blank=True)
    size_2=models.CharField(max_length=200,null=True,blank=True)
    size_3=models.CharField(max_length=200,null=True,blank=True)
    size_4=models.CharField(max_length=200,null=True,blank=True)
    size_5=models.CharField(max_length=200,null=True,blank=True)
    size_6=models.CharField(max_length=200,null=True,blank=True)
    delivery_charges=models.IntegerField()
    


    description = models.TextField(null=True,blank=True)
 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    trending=models.BooleanField(default=False)
    number = models.PositiveIntegerField( null=True,blank=True)
    soled=models.IntegerField(null=True,blank=True)
    discount=models.BooleanField(default=False,null=True,blank=True)
    percentage=models.PositiveIntegerField(null=True,blank=True)
    original=models.PositiveIntegerField(null=True,blank=True)
    volume = models.CharField(max_length=10,null=True,blank=True)

    #class Meta:
        #ordering = ('shu',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'listings:product_detail',
            args=[self.category.slug, self.slug]
        )

    def get_average_review_score(self):
        average_score = 0.0
        if self.reviews.count() > 0:
            total_score = sum([review.rating for review in self.reviews.all()])
            average_score = total_score / self.reviews.count()
        return round(average_score, 1)

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=50)
        
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
class Return(models.Model):
    product_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    date_and_time_of_purchasing = models.CharField(max_length=55)
    city = models.CharField(max_length=200)
    def __str__(self):
        return self.product_name

