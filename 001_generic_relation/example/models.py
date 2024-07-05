from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class YourFirst(models.Model):
    mains = GenericRelation('example.YourMain', related_query_name='first', related_name='firsts')


class YourSecond(models.Model):
    mains = GenericRelation('example.YourMain', related_query_name='second', related_name='seconds')


class YourMain(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
