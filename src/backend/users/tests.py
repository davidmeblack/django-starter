from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def test_create_user(self):
        '''Test creating a user'''
        User = get_user_model()
        user = User.objects.create_user(
            username='test-user',
            password='test'
        )

        self.assertEqual(user.username, 'test-user')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        '''Test creating a superuser'''
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username='test-super',
            password='test'
        )

        self.assertEqual(superuser.username, 'test-super')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
