from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.
class PostAPITest(APITestCase):
    def test_create_post(self) -> None:
        url = reverse('post-list')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post',
            'author': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.data['content'], 'This is a test post')
        self.assertEqual(response.data['author'], 1)
