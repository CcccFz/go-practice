from django.test import TestCase
from django.core.urlresolvers import resolve
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo
from .views import TodoViewSet


# 模块级测试固件
def setUpModule():
    Todo.create('first todo')


class TodoViewTest(TestCase):

    def test_view_set(self):
        func = resolve('/api/todos/').func
        self.assertEquals(func.__name__, TodoViewSet.__name__)


class TodoModelTest(TestCase):

    def test_get(self):
        todo = Todo.get(1)
        self.assertEquals(todo.title, 'first todo')

    def test_create(self):
        Todo.create('second todo')
        self.assertEquals(Todo.get(1).title, 'first todo')
        self.assertEquals(Todo.get(2).title, 'second todo')

    def test_all(self):
        todos = Todo.all()
        self.assertEquals(len(todos), 1)

        Todo.create('second todo')
        todos = Todo.all()
        self.assertEquals(len(todos), 2)

    def test_remove(self):
        todos = Todo.all()
        self.assertEquals(len(todos), 1)

        Todo.remove(1)
        todos = Todo.all()
        self.assertEquals(len(todos), 0)


class TodoApiTest(APITestCase):

    def test_get(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        self.assertEqual(Todo.objects.count(), 1)

        response = self.client.post('/api/todos/', {'title': 'second todo'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)

    def test_input_empty_title(self):
        response = self.client.post('/api/todos/', {'title': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_input_title_over_255(self):
        response = self.client.post('/api/todos/', {'title': 'a' * 256}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        response = self.client.delete('/api/todos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)