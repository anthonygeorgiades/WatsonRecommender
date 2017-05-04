from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField(null=True)
    sentiment = models.TextField(null=True)
    sentimentValue = models.FloatField(null=True)
    date = models.DateTimeField(null=True)

    def __unicode__(self):
        return str(self.id)

