from django.db import models

# Create your models here.


class Role(models.Model):
    rolename = models.CharField(max_length=255, default='user')

    def __str__(self):
        return self.rolename

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, related_name='role', on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.username