from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Tone(models.Model):
    id = models.AutoField(primary_key=True)
    tone_json = models.TextField(null=True)
    is_prediction_correct = models.NullBooleanField()
    date = models.DateTimeField(null=True)

    def __unicode__(self):
        return str(self.id)


