from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Head0 = models.CharField(max_length=500,default="")
    ConHead0 = models.CharField(max_length=50000, default="")
    Head1 = models.CharField(max_length=500,default="")
    ConHead1 = models.CharField(max_length=50000, default="")
    Head2 = models.CharField(max_length=500,default="")
    ConHead2 = models.CharField(max_length=50000, default="")
    pub_Date = models.DateField()
    Thumbnail = models.ImageField(upload_to="Shop/images",default="")

    def __str__(self):
        return self.Title