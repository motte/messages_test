from django.db import models


class Message(models.Model):
    state = models.CharField('State', max_length=64)
    state_abbreviation = models.CharField('Abbreviation', max_length=2)
    city = models.CharField('City', max_length=64)
    username = models.CharField('User', max_length=64)
    message = models.TextField('Message')
    create_time = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        ordering = ['state', 'city', 'create_time']
