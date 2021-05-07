from django.db import models

class User(models.Model):
    fb_id = models.IntegerField(max_length=64)
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True, default=None)
    google_token = models.TextField()
    subscribe = models.BooleanField(default=False)
    activity_category = models.ForeignKey("ActivityCategory", on_delete=models.SET_NULL, null=True, default=None)


class FastLink(models.Model):
    name = models.TextField()
    url = models.TextField()


class Log(models.Model):
    log = models.JSONField()


class State(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("State", on_delete=models.CASCADE)
    function = models.CharField(max_length=64)
    is_input = models.BooleanField(default=False)


class ActivityCategory(models.Model):
    name = models.CharField(max_length=8)
