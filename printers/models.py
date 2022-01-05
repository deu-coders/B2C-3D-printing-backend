from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Printer(models.Model):
    id = models.AutoField(primary_key=True)
    model_image = models.ImageField(null=False)
    model_name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(blank=False, null=False)
    filament_remain = models.IntegerField(null=False, default=0)
    STATE_CHOICE = (("비활성화", "비활성화"), ("활성화", "활성화"))
    state = models.CharField(max_length=200, null=False, default='비활성화', choices=STATE_CHOICE)
    process = models.IntegerField(null=False, default=0)
    requestment = models.ForeignKey('Requestment', related_name='printers', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.id}] {self.model_name}'

class Requestment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(), related_name='requestments', null=True, on_delete=models.SET_NULL)
    comment = models.TextField(null=False, default='')
    printer = models.ForeignKey('Printer', related_name='requestments', null=True, on_delete=models.SET_NULL)
    STATE_CHOICE = (("준비중", "준비중 "), ("완료", "완료"), ("배송중", "배송중"))
    state = models.CharField(max_length=200, null=False, default='준비중', choices=STATE_CHOICE)
    model_file = models.FileField(null=False)

    def __str__(self):
        return f'[{self.id}] {self.author} :: {self.printer.model_name}'