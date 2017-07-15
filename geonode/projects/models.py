from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

import datetime


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    sname = models.CharField(
        # A short name field
        max_length=30,
        null=True,
        blank=True,
        help_text="Short name for project, example KCEP or CCRP"
    )
    description = models.TextField()
    organization = models.CharField(max_length=150)
    start_date = models.DateField(
        default=timezone.now,  # datetime.date.today(),
        help_text="Please define the date that the project was initiated"
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Leave blank if project is still continuing"
    )
    image = models.ImageField(upload_to='images/')

    STATUS_CHOICES = (
        ('ON', 'Ongoing'),
        ('CP', 'Completed'),
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='ON'
    )

    published_date = models.DateTimeField(
        auto_now_add=True
    )

    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def get_layers(self):
        layers = self.layer_set.all()
        return layers

    def get_documents(self):
        documents = self.document_set.all()
        return documents

    def get_maps(self):
        maps = []
        layers = self.get_layers()

        for layer in layers:
            related_maps = layer.maps()
            maps += related_maps

        # return a filtered out unique set of maps
        return list(set(maps))

    def get_url(id):
        """ get url to project. difference to get_absolute_url?? """
        id = id
        return reverse('project_detail', kwargs={'pk': id})

    def get_absolute_url(self):
        # return reverse('project_list')
        return reverse('project_detail', kwargs={'pk': self.pk})

    def get_status(self):
        if self.status == 'ON':
            return 'Ongoing'
        return 'Completed'

    def publish(self):
        if self.start_date > self.end_date:
            pass
        self.save()

    def destroy(self):
        self.delete()
