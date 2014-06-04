from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post


class PostTest(TestCase):

    def test_create_empty_post(self):
        # create a new empty post
        post = Post()
        post.save()
        all_posts = Post.objects.all()
        first_post = all_posts[0]
        self.assertEqual(post, first_post)

    def test_create_post(self):
        # Create the post
        post = Post()

        # Set the attributes
        post.title = 'My first post'
        post.text = 'This is my first post that is so awesome'
        post.pub_date = timezone.now()

        # Save it
        post.save()

        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)

        # Check attributes
        self.assertEqual(only_post.title, 'My first post')
        self.assertEqual(only_post.text, 'This is my first post that is so awesome')
        self.assertEqual(only_post.pub_date.day, post.pub_date.day)
        self.assertEqual(only_post.pub_date.month, post.pub_date.month)
        self.assertEqual(only_post.pub_date.year, post.pub_date.year)
        self.assertEqual(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEqual(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEqual(only_post.pub_date.second, post.pub_date.second)

class AdminTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'Jack'
        self.email = 'test@test.com'
        self.password = 'adit'
        self.test_user = User.objects.create_superuser(self.username, self.email, self.password)

    def test_page_admin_exists(self):
        # Get login page
        response = self.client.get('/admin/')

        # Check response code
        self.assertEqual(response.status_code, 200)
        self.assertTrue(bytes('Log in', 'utf-8') in response.content)

    def test_login(self):
        login = self.client.login(username='Jack', password='adit')
        self.assertTrue(login)
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(bytes('Log out', 'utf-8') in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username='Jack', password="adit")

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue(bytes('Log out', 'utf-8') in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue(bytes('Log in', 'utf-8') in response.content)