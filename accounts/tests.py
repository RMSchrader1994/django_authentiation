from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestAccounts(TestCase):
    def test_anonymous_user_can_not_view_profile(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_view_profile(self):
        user = User.objects.create_user('user', 'user@example.com', 'user')
        self.client.login(username="user", password="user")

        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")


Add CommentCollapse 

richardadalton10:34 AM
from django.contrib.auth.decorators import login_required
