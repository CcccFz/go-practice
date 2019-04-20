from django.db import models


# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    title = models.CharField(verbose_name="标题", max_length=255)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def get(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def create(cls, title):
        return cls.objects.create(title=title)

    @classmethod
    def remove(cls, pk):
        todo = cls.get(pk)
        todo.delete()

    def __str__(self):
        created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        return 'Created_At: {created_at}, {title}'.format(created_at=created_at, title=self.title)
