from django.db import models
from django.urls import reverse


# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('branch_name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def get_url(self):
        return reverse('taskapp:branch_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.branch_name)


class Sub_Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subbranch'
        verbose_name_plural = 'subbranches'

    def get_url(self):
        return reverse('taskapp:sub', args=[self.branch.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
