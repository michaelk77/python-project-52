from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse


# Create your tests here.


class Crud_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name='random',
            last_name='user',
            username='abc',
            password='123'
        )
        User.objects.create(
            first_name='vlad',
            last_name='kiborg',
            username='t1000',
            password='skinet'
        )

    def test_Sign_Up(self):
        resp = self.client.get(reverse('sign_up'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('sign_up'),
            {
                'first_name': 'Name',
                'last_name': 'monster',
                'username': 'makeit',
                'password1': 'smallpass',
                'password2': 'smallpass',
            }
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))
        user = User.objects.last()
        self.assertEqual(user.last_name, 'monster')
        self.assertEqual(user.username, 'makeit')

    def test_UpdateUser(self):
        user = User.objects.get(id=1)
        resp = self.client.get(
            reverse('user_update', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))
        self.client.force_login(user)
        resp = self.client.get(
            reverse('user_update', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('user_update', kwargs={'pk': user.id}),
            {
                'first_name': 'vlad',
                'last_name': 'ggg',
                'username': '12345',
                'password1': 'hihi',
                'password2': 'hihi',
            })
        self.assertEqual(resp.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'vlad')

    def test_DelUser(self):
        user = User.objects.get(username='t1000')
        resp = self.client.get(reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))
        self.client.force_login(user)
        resp = self.client.get(reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('user_delete', kwargs={'pk': user.id}))
        self.assertRedirects(resp, reverse('home'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def testViewUsers(self):
        resp = self.client.get(reverse('users'))
        user = User.objects.get(username='t1000')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, user.first_name)
