from django.db import models

class User(models.Model):
    fb_id = models.TextField()
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    token = models.TextField(null=True, blank=True)
    subscribed = models.BooleanField(default=False)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True, default=None, blank=True)


class Link(models.Model):
    name = models.TextField()
    title = models.TextField()
    discription = models.TextField()
    button_label = models.TextField()
    img_url = models.TextField()
    url = models.TextField()


class Log(models.Model):
    log = models.JSONField()


class State(models.Model):
    name = models.CharField(max_length=128)
    label = models.TextField(null=True, blank=True)
    prompt = models.TextField(null=True, blank=True, default=None)
    parent = models.ForeignKey("State", on_delete=models.CASCADE, null=True, blank=True)
    function = models.CharField(max_length=64, blank=True)
    is_input = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.label


class Role(models.Model):
    name = models.CharField(max_length=8)


class Contact(models.Model):
    fb_id = models.TextField()
    contact = models.JSONField()
