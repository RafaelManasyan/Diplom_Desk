from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from addesk.models import Advert, Review

User = get_user_model()


class AdvertAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser@test.com", password="password")
        self.client.force_authenticate(user=self.user)
        self.advert = Advert.objects.create(
            author=self.user,
            title="test1",
            description="test2description"
        )

    def test_advert_list(self):
        """Тест для AdvertListAPIView"""
        url = reverse("desk:advert-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data.get("results", [])) >= 1)

    def test_create_advert(self):
        """Тест для AdvertCreateAPIView"""
        url = reverse('desk:advert-create')
        data = {
            'title': 'Test Advert',
            'description': 'Test description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Advert')
        self.assertEqual(response.data['description'], 'Test description')

    def test_retrieve_advert(self):
        """Тест для AdvertRetrieveUpdateDestroyAPIView"""
        url = reverse('desk:advert-detail', args=[self.advert.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.advert.title)
        self.assertEqual(response.data['description'], self.advert.description)

    def test_update_advert(self):
        """Тест для обновления объявления"""
        url = reverse('desk:advert-detail', args=[self.advert.id])
        data = {'title': 'Updated Title', 'description': 'Updated Description'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')
        self.assertEqual(response.data['description'], 'Updated Description')

    def test_delete_advert(self):
        """Тест для удаления объявления"""
        url = reverse('desk:advert-detail', args=[self.advert.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReviewListAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser@test.com", password="password")
        self.client.force_authenticate(user=self.user)

        self.advert = Advert.objects.create(
            author=self.user,
            title="Test Advert",
            description="Test description"
        )

        self.review = Review.objects.create(
            author=self.user,
            text="Test review",
            advert=self.advert)

    def test_review_list(self):
        """Тест для ReviewListAPIView"""
        url = reverse('desk:review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_create_review(self):
        """Тест для ReviewCreateAPIView"""
        url = reverse('desk:review-create')
        data = {
            'text': 'Test review text',
            'advert': self.advert.id
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_review(self):
        """Тест для получения отзыва"""
        url = reverse('desk:review-detail', args=[self.review.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.review.text)

    def test_update_review(self):
        """Тест для обновления отзыва"""
        url = reverse('desk:review-detail', args=[self.review.id])
        data = {'text': 'Updated review text'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Updated review text')

    def test_delete_review(self):
        """Тест для удаления отзыва"""
        url = reverse('desk:review-detail', args=[self.review.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)