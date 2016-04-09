from __future__ import unicode_literals

from django.db import models


class MigrateVersion(models.Model):
    repository_id = models.CharField(primary_key=True, max_length=250)
    repository_path = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrate_version'


class Store(models.Model):
    topic = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'
        get_latest_by = 'timestamp'
