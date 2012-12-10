import uuid
from django.test import TestCase
from django.utils import timezone
from devices.models import Device


class DeviceTest(TestCase):
    def test_creating_device_and_saving_it(self):
        device = Device()
        device.name = "Device 1"
        device.registered_at = timezone.now()
        device.save()

        # Retreive it
        all_devices = Device.objects.all()
        self.assertEquals(len(all_devices), 1)
        self.assertEquals(all_devices[0].name, "Device 1")
        self.assertIsInstance(uuid.UUID(all_devices[0].uuid), uuid.UUID)
        self.assertEquals(all_devices[0].registered_at, device.registered_at)

    def test_verbose_name_for_pub_date(self):
        for field in Device._meta.fields:
            if field.name ==  'uuid':
                self.assertEquals(field.verbose_name, 'Device ID')

    def test_repr_looks_ok(self):
        device = Device()
        device.name = "Device 1"
        device.registered_at = timezone.now()
        self.assertTrue(unicode(device).startswith("Device 1 -"))



