from django.db import models

class User(models.Model):
    fb_id = models.TextField()
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    token = models.TextField(null=True, blank=True)
    subscribed = models.BooleanField(default=False)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True, default=None, blank=True)


class Link(models.Model):
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


class Role(models.Model):
    name = models.CharField(max_length=8)
