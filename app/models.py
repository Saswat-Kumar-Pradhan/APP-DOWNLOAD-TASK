from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class App(models.Model):
    app_pic = models.ImageField(upload_to='app_image') 
    app_name = models.CharField(max_length=50, unique=True)
    app_link = models.CharField(max_length=200)

    CATEGORY_CHOICES = (
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Productivity', 'Productivity'),
        ('Food', 'Food'),
        ('Medical', 'Medical'),
        ('Lifestyle', 'Lifestyle'),
        ('Entertainment', 'Entertainment'),
        ('Communication', 'Communication'),
        ('Finance', 'Finance'),
        ('Other', 'Other'),
    )

    SUB_CATEGORY_CHOICES = (
        ('Travel', 'Travel'),
        ('Magazines', 'Magazines'),
        ('Books', 'Books'),
        ('Gaming', 'Gaming'),
        ('Social Media', 'Social Media'),
        ('Music', 'Music'),
        ('Photo and video', 'Photo and video'),
        ('Web apps', 'Web apps'),
        ('Reference', 'Reference'),
        ('Dating', 'Dating'),
        ('Other', 'Other'),
    )
    catagory = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    sub_catagory = models.CharField(max_length=30, choices=SUB_CATEGORY_CHOICES)
    points = models.IntegerField()

    def __str__(self):
        return self.app_name
    
class AppTask(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots') 

    def __str__(self):
        return f"Task for {self.aid.app_name} by {self.uid.name}"
