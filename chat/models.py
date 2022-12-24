from django.db import models


class chatRoom(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name = 'Chat Room'