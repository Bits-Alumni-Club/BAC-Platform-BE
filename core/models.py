from django.db import models


# Create your models here.

class Home(models.Model):
    # heading = models.xxxx
    # paragraph = models.xxx
    # slide_image = models.xxx
    # active = models.xxx this hould be true or false
    # display_time = models.xxx will be use to control period for image to show
    pass


class WhoWeAre(models.Model):
    # headlines = models.xxx
    # paragraph = models.xxx
    # image = models.xxx
    # active = models.xxx
    pass


class Vision(models.Model):
    # paragraph = models.xxx
    # active = models.xxx
    pass


class Mission(models.Model):
    # paragraph = models.xxx
    # active = models.xxx
    pass


class Team(models.Model):
    # user = models.xxxx
    # heading = models.xxx
    # paragraph = models.xxx
    # active = models.xxx
    pass


class Contact(models.Model):
    pass


class FAQ(models.Model):
    pass