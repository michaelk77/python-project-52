from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.tasks.models import Task


# Create your tests here.
class CRUD_Task(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='johndoe', password='pass'
        )
        Status.objects.create(name='a1')
        self.task1 = Task.objects.create(
            name='task1', description='task1 description', author=self.user,
            executor=self.user, status=Status.objects.get(id=1)
        )
        self.task2 = Task.objects.create(
            name='task2', description='task2 description', author=self.user,
            executor=self.user, status=Status.objects.get(id=1)
        )

    def test_access(self):
        resp1 = self.client.get(reverse('tasks'))
        self.assertEqual(resp1.status_code, 302)

        resp2 = self.client.get(reverse('task_create'))
        self.assertEqual(resp2.status_code, 302)

        resp3 = self.client.get(reverse('task_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)

        resp4 = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)

        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('tasks'))
        self.assertEqual(resp1.status_code, 200)

        resp2 = self.client.get(reverse('task_create'))
        self.assertEqual(resp2.status_code, 200)

        resp3 = self.client.get(reverse('task_update', kwargs={'pk': 2}))
        self.assertEqual(resp3.status_code, 200)

        resp4 = self.client.get(reverse('task_delete', kwargs={'pk': 2}))
        self.assertEqual(resp4.status_code, 200)

    def test_list(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(len(resp.context['tasks']), 2)

    def test_create(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('task_create'), {
            'name': 'task3',
            'description': 'task3 description',
            'status': '1', 'author': '1', 'executor': '1'
        })
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('tasks'))
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(len(resp.context['tasks']), 3)

    def test_update(self):
        self.client.force_login(self.user)
        task1 = Task.objects.get(pk=1)
        resp = self.client.post(reverse('task_update', kwargs={'pk': 1}), {
            'name': 'updated task',
            'description': 'updated task description',
            'status': '1', 'author': '1', 'executor': '1'
        })
        self.assertEqual(resp.status_code, 302)
        task1.refresh_from_db()
        self.assertEqual(task1.name, 'updated task')
        self.assertEqual(task1.description, 'updated task description')

    def test_delete(self):
        self.client.force_login(self.user)
        self.assertEqual(Task.objects.count(), 2)
        resp = self.client.post(reverse('task_delete', kwargs={'pk': 2}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(pk=1).name, 'task1')
