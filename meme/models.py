from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Meme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    username = "anonymous"
    post = models.ImageField(upload_to='anon_m')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return Meme.username

    def get_absolute_url(self):
        return reverse("memes:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-creation_date"]