from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# -- coding: UTF-8 --
class Products(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField(max_length = 200) 
    pub_date = models.DateField()
    votes_total = models.IntegerField(default=1)
    body =  models.TextField()
    image = models.ImageField(upload_to='uploads/')
    iconImage = models.ImageField(upload_to='uploads/')
    upvoted = models.BooleanField()
    changedBy = models.ForeignKey(User, on_delete= models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
     
    def hunter(self):
        return self.body[:10]

    def summary(self):
        return self.body[:500]
