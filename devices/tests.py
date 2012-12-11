import uuid
from django.test import TestCase
from django.utils import timezone
from devices.models import Device, Space


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


class SpaceTest(TestCase):
    def create_space(self):
        device = Device()
        device.name = "Device 1"
        device.registered_at = timezone.now()
        device.save()
        space = Space()
        space.device = device
        space.name = "Space 1"
        space.area = 22.5
        space.save()
        return space

    def teardown(self):
        pass

    def test_creating_a_space_and_saving_it(self):
        space = self.create_space()
        space.save()
        all_spaces = Space.objects.all()
        self.assertEquals(len(all_spaces), 1)
        self.assertIsInstance(space.area, float)

    def test_repr_looks_ok(self):
        space = self.create_space()
        self.assertTrue(unicode(space).startswith("Space 1 -"))










