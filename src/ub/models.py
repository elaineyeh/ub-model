from django.db import models

class User(models.Model):
    fb_id = models.TextField()
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    google_token = models.TextField(null=True, blank=True)
    subscribe = models.BooleanField(default=False)
    activity_category = models.ForeignKey("ActivityCategory", on_delete=models.SET_NULL, null=True, default=None, blank=True)


class FastLink(models.Model):
    name = models.TextField()
    discription = models.TextField(null=True, blank=True)
    button_label = models.TextField(null=True, blank=True)
    url = models.TextField()


class Log(models.Model):
    log = models.JSONField()


class State(models.Model):
    name = models.CharField(max_length=128)
    label = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("State", on_delete=models.CASCADE, null=True, blank=True)
    function = models.CharField(max_length=64, blank=True)
    is_input = models.BooleanField(default=False)


class ActivityCategory(models.Model):
    name = models.CharField(max_length=8)
