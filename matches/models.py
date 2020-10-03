from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

class Match(models.Model):
    op_name = models.CharField(max_length=200)
    op_email = models.EmailField(max_length=200)
    op_number = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    money_needed = models.PositiveSmallIntegerField()
    money_spending = models.PositiveSmallIntegerField()
    store = models.CharField(max_length=200)
    resolved = models.BooleanField()
    def __str__(self):
        return self.op_name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_absolute_url(self):
        return reverse('matches:matchdetail', args=(self.id,))