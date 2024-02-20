from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Wig

class WigTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.client.force_authenticate(user=self.user)
        self.wig_data = {
            'name': 'Test Wig',
            'color': 'Black',
            'length': '10.00',
            'curl_pattern': 'curly',
            'density': '50.00',
            'hair_origin': 'brazilian',
            'description': 'A beautiful test wig',
            'price': '100.00',
            'owner': self.user,  # Use the user instance instead of user.id
        }

        # Create a wig owned by the user
        self.wig = Wig.objects.create(**self.wig_data)


    def test_create_wig(self):
        self.wig_data['owner'] = self.user.id
        response = self.client.post('/api/wigs/', self.wig_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


    def test_get_wig_list(self):
        response = self.client.get('/api/wigs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wig_by_id(self):
        response = self.client.get(f'/api/wigs/{self.wig.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_wig(self):
        # Create a new user for ownership
        new_user = get_user_model().objects.create_user(
            username='newuser',
            password='newpassword'
        )
        # Update data, including the owner field
        updated_data = {
            'name': 'Updated Test Wig',
            'color': 'Brown',
            'length': '20.00',
            'curl_pattern': 'straight',
            'density': '70.00',
            'hair_origin': 'peruvian',
            'description': 'An updated test wig',
            'price': '150.00',
            'owner': new_user.id,
        }

        response = self.client.put(f'/api/wigs/{self.wig.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_delete_wig(self):
        response = self.client.delete(f'/api/wigs/{self.wig.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
