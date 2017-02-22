from django.db import models


class Meme(models.Model):
    #user = models.ForeignKey(blank=True, null=True)
    username = "anonymous"
    post = models.ImageField(upload_to='anon_m')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return Meme.username
