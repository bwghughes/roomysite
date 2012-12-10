from django.db import models
from django.db import models
import uuid


class UUIDField(models.CharField) :

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64)
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)

class Device(models.Model):
    uuid = UUIDField(verbose_name='Device ID')
    name = models.CharField(max_length=200)
    registered_at = models.DateTimeField()

    def __unicode__(self):
        return "{0} - {1}".format(self.name, self.uuid)
