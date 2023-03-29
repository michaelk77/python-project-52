from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User


# Create your tests here.
class CRUD_Status(TestCase):
    def setUp(self):
        User.objects.create(
            first_name='fedor',
            last_name='qwerty',
            username='robot',
            email='all@gmail.com',
            password='abcd'
        )
        self.user = User.objects.get(id=1)
        Status.objects.create(name='a1')
        Status.objects.create(name='a2')
        Status.objects.create(name='a3')

    def test_access(self):
        resp1 = self.client.get(reverse('statuses'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('status_create'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)
        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('statuses'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('status_create'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('status_update', kwargs={'pk': 2}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('status_delete', kwargs={'pk': 2}))
        self.assertEqual(resp4.status_code, 200)

    def test_List(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 3)

    def test_Create(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('status_create'), {'name': 'status4'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('statuses'))
        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 4)

    def test_Update(self):
        self.client.force_login(self.user)
        s1 = Status.objects.get(pk=1)
        resp = self.client.post(reverse('status_update', kwargs={'pk': 1}),
                                {'name': 'new Status'})
        self.assertEqual(resp.status_code, 302)
        s1.refresh_from_db()
        self.assertEqual(s1.name, 'new Status')

    def test_Delete(self):
        self.client.force_login(self.user)
        self.assertEqual(Status.objects.count(), 3)
        resp = self.client.post(
            reverse('status_delete', kwargs={'pk': 3})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.get(pk=1).name, 'a1')
        self.assertEqual(Status.objects.get(pk=2).name, 'a2')
