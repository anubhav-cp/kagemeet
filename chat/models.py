from django.db import models


class chatRoom(models.Model):
    name = models.CharField(max_length=150)
    channel_description = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name = 'Chat Room'