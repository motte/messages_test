from django.db import models
import datetime


class Message(models.Model):
    state = models.CharField('State', max_length=64)
    state_abbreviation = models.CharField('Abbreviation', max_length=2)
    city = models.CharField('City', max_length=64)
    username = models.CharField('User', max_length=64)
    message = models.TextField('Message')
    create_time = models.DateTimeField('Date', default=datetime.datetime.now)
    is_deleted = models.BooleanField('Deleted', default=False)

    class Meta:
        ordering = ['state', 'city', 'create_time']

    def __unicode__(self):
        return u'%s - %s - %s' % (self.create_time, self.username, self.message[:30])

    def save(self, *args, **kwargs):
        exists = City.objects.get_or_create(name=self.city)
        count = MessageStat.objects.filter(pk=1).update(total_messages=F(total_messages)+1)
        super(Message, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        count = MessageStat.objects.filter(pk=1).update(total_messages=F(total_messages)-1)
        super(Message, self).delete(*args, **kwargs)


class City(models.Model):
    """
    Future GIS information could be added here, make sure to use South
    """
    name = ''

    class Meta:
        ordering = ['']
        verbose_name_plural = 'cities'


class MessageStat(models.Model):
    """
    Use counters just in case of enormous data sets with very high throughput
    - NOT efficient for smaller datasets
    """
    total_messages = models.BigIntegerField('Total Messages')
    total_cities = models.BigIntegerField('Total Cities')
    total_users = models.BigIntegerField('Total Users')

    class Meta:
        ordering = ['total_messages', 'total_cities', 'total_users']
