from django.db import models

# Create your models here.
class Performer(models.Model):
    name = models.CharField(max_length=255)
    # performer = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    performer = models.ForeignKey(Performer)

    class Meta:
        ordering = ['order',]
    #duration = models.DurationField()

    def __str__(self):
        return '{} by {}'.format(self.title, self.artist)
