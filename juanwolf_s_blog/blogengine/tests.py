from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post, Category, Tag
import feedparser


class PostTest(TestCase):
    def test_create_category(self):
        # Create the category
        category = Category()

        # Add attributes
        category.name = 'python'
        category.description = 'The Python programming language'

        # Save it
        category.save()

        # Check we can find it
        all_categories = Category.objects.all()
        self.assertEqual(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEqual(only_category, category)

        # Check attributes
        self.assertEqual(only_category.name, 'python')
        self.assertEqual(only_category.description, 'The Python programming language')

    def test_create_tag(self):
        # Create the tag
        tag = Tag()

        # Add attributes
        tag.name = 'python'
        tag.description = 'The Python programming language'

        # Save it
        tag.save()

        # Check we can find it
        all_tags = Tag.objects.all()
        self.assertEqual(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEqual(only_tag, tag)

        # Check attributes
        self.assertEqual(only_tag.name, 'python')
        self.assertEqual(only_tag.description, 'The Python programming language')


    def test_create_post(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the post
        post = Post()

        # Set the attributes
        post.title = 'My first post'
        post.text = 'This is my first post that is so awesome'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
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
        self.assertEqual(only_post.category.name, 'python')
        self.assertEqual(only_post.category.description, 'The Python programming language')

        # Check tags
        post_tags = only_post.tags.all()
        self.assertEqual(len(post_tags), 1)
        only_post_tag = post_tags[0]
        self.assertEqual(only_post_tag, tag)
        self.assertEqual(only_post_tag.name, 'python')
        self.assertEqual(only_post_tag.description, 'The Python programming language')


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
        self.assertEqual(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue(bytes('Log out', 'utf-8') in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue(bytes('Log in', 'utf-8') in response.content)

    def test_create_category(self):
        # Log in
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)

        # Check response code
        response = self.client.get('/admin/blogengine/category/add/')
        self.assertEqual(response.status_code, 200)

        # Create the new category
        response = self.client.post('/admin/blogengine/category/add/', {
            'name': 'python',
            'description': 'The Python programming language'}
            , follow=True)
        self.assertEqual(response.status_code, 200)

        # Check added successfully
        self.assertTrue(bytes('added successfully', 'utf-8') in response.content)

        # Check new category now in database
        all_categories = Category.objects.all()
        self.assertEqual(len(all_categories), 1)

    def test_edit_category(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Log in
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)

        # Edit the category
        response = self.client.post('/admin/blogengine/category/' + str(category.id) + '/', {
            'name': 'perl',
            'description': 'The Perl programming language'}
            , follow=True)
        self.assertEqual(response.status_code, 200)

        # Check changed successfully
        self.assertTrue(bytes('changed successfully', 'utf-8') in response.content)

        # Check category amended
        all_categories = Category.objects.all()
        self.assertEqual(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEqual(only_category.name, 'perl')
        self.assertEqual(only_category.description, 'The Perl programming language')

    def test_delete_category(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Log in
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        # Delete the category
        response = self.client.post('/admin/blogengine/category/' + str(category.id) + '/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue(bytes('deleted successfully', 'utf-8') in response.content)

        # Check category deleted
        all_categories = Category.objects.all()
        self.assertEqual(len(all_categories), 0)


    def test_create_tag(self):
        # Log in
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        # Check response code
        response = self.client.get('/admin/blogengine/tag/add/')
        self.assertEqual(response.status_code, 200)

        # Create the new tag
        response = self.client.post('/admin/blogengine/tag/add/', {
            'name': 'python',
            'description': 'The Python programming language'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check added successfully
        self.assertTrue(bytes('added successfully', 'utf-8') in response.content)

        # Check new tag now in database
        all_tags = Tag.objects.all()
        self.assertEqual(len(all_tags), 1)

    def test_edit_tag(self):
        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Log in
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)

        # Edit the tag
        response = self.client.post('/admin/blogengine/tag/' + str(tag.id) + '/', {
            'name': 'perl',
            'description': 'The Perl programming language'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check changed successfully
        self.assertTrue(bytes('changed successfully', 'utf-8') in response.content)

        # Check tag amended
        all_tags = Tag.objects.all()
        self.assertEqual(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEqual(only_tag.name, 'perl')
        self.assertEqual(only_tag.description, 'The Perl programming language')

    def test_delete_tag(self):
        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Log in
        logged = self.client.login(username=self.username, password=self.password)
        self.assertTrue(logged)

        # Delete the tag
        response = self.client.post('/admin/blogengine/tag/' + str(tag.id) + '/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue(bytes('deleted successfully', 'utf-8') in response.content)

        # Check tag deleted
        all_tags = Tag.objects.all()
        self.assertEqual(len(all_tags), 0)



    def test_create_post(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        response = self.client.get('/admin/blogengine/post/add/')
        self.assertEqual(response.status_code, 200)

        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the new post
        response = self.client.post('/admin/blogengine/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2014-06-05',
            'pub_date_1': '00:00:04',
            'slug': 'my-first-post',
            'category': str(category.id),
            'tags': str(tag.id),
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check added successfully
        self.assertTrue(bytes('added successfully', 'utf-8') in response.content)

        # Check new post now in database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)

    def test_edit_post(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()
        # Log in
        self.client.login(username=self.username, password=self.password)
        post_exists = self.client.get('/admin/blogengine/post/' + str(post.id) + '/')
        self.assertTrue(post_exists)

        # Edit the post
        response = self.client.post('/admin/blogengine/post/' + str(post.id) + '/', {
            'title': 'My second post',
            'text': 'This is my second blog post',
            'pub_date_0': '2014-06-04',
            'pub_date_1': '22:00:04',
            'slug': 'my-first-post',
            'category': category.id,
            'tags': tag.id,
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check changed successfully
        self.assertTrue(bytes('changed successfully', 'utf-8') in response.content)

        # Check post amended
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post.title, 'My second post')
        self.assertEqual(only_post.text, 'This is my second blog post')

    def test_delete_post(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)

        # Log in
        self.client.login(username=self.username, password=self.password)

        # Delete the post
        response = self.client.post('/admin/blogengine/post/' + str(post.id) + '/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue(bytes('deleted successfully', 'utf-8') in response.content)

        # Check post amended
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 0)


class PostViewTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'perl'
        tag.description = 'The Perl programming language'
        tag.save()



        # Create the post
        post = Post()
        post.title = "My first post !!"
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()

        # Check post saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        self.assertEqual(all_posts[0], post)

        # Check the index response
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # Check the content of the page
        self.assertTrue(bytes(post.title, 'utf-8') in response.content)
        self.assertTrue(bytes(post.text, 'utf-8') in response.content)

        # Check the post category is in the response
        self.assertTrue(bytes(post.category.name, 'utf-8') in response.content)

        # Check the post tag is in the response
        post_tag = all_posts[0].tags.all()[0]
        self.assertTrue(bytes(post_tag.name, 'utf-8') in response.content)

        self.assertTrue(bytes(str(post.pub_date.year), 'utf-8') in response.content)
        self.assertTrue(bytes(str(post.pub_date.strftime('%b')), 'utf-8') in response.content)
        self.assertTrue(bytes(str(post.pub_date.day), 'utf-8') in response.content)

        # Check the link is marked up properly
        self.assertTrue(
            bytes('<a href="http://127.0.0.1:8000/">my first blog post</a>', 'utf-8')
            in response.content)

    def test_post_page(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'perl'
        tag.description = 'The Perl programming language'
        tag.save()

        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)

        # Get the post URL
        post_url = only_post.get_absolute_url()

        # Fetch the post
        response = self.client.get(post_url)
        self.assertEqual(response.status_code, 200)

        # Check the post title is in the response
        self.assertTrue(bytes(post.title, 'utf-8') in response.content)

        # Check the post text is in the response
        self.assertTrue(bytes(post.text, 'utf-8') in response.content)
        # Check the category is in the response
        self.assertTrue(bytes(post.category.name, 'utf-8') in response.content)
        # Check the post tag is in the response
        post_tag = all_posts[0].tags.all()[0]
        self.assertTrue(bytes(post_tag.name, 'utf-8') in response.content)


        # Check the post date is in the response
        self.assertTrue(bytes(str(post.pub_date.year), 'utf-8') in response.content)
        self.assertTrue(bytes(post.pub_date.strftime('%b'), 'utf-8') in response.content)
        self.assertTrue(bytes(str(post.pub_date.day), 'utf-8') in response.content)

        # Check the link is marked up properly
        self.assertTrue(
            bytes('<a href="http://127.0.0.1:8000/">my first blog post</a>', 'utf-8')
            in response.content)

    def test_category_page(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.category = category
        post.save()

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)

        # Get the category URL
        category_url = post.category.get_absolute_url()

        # Fetch the category
        response = self.client.get(category_url)
        self.assertEqual(response.status_code, 200)

        # Check the category name is in the response
        self.assertTrue(bytes(post.category.name, 'utf-8') in response.content)

        # Check the post text is in the response
        self.assertTrue(bytes(post.text, 'utf-8') in response.content)

        # Check the post date is in the response
        self.assertTrue(bytes(str(post.pub_date.year), 'utf-8') in response.content)
        self.assertTrue(bytes(post.pub_date.strftime('%b'), 'utf-8') in response.content)
        self.assertTrue(bytes(str(post.pub_date.day), 'utf-8') in response.content)

        # Check the link is marked up properly
        self.assertTrue(bytes('<a href="http://127.0.0.1:8000/">my first blog post</a>',
                              'utf-8') in response.content)

    def test_tag_page(self):
        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()


        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.save()
        post.tags.add(tag)
        post.save()

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)

        # Get the tag URL
        tag_url = post.tags.all()[0].get_absolute_url()

        # Fetch the tag
        response = self.client.get(tag_url)
        self.assertEqual(response.status_code, 200)

        # Check the tag name is in the response
        self.assertTrue(bytes(post.tags.all()[0].name, 'utf-8') in response.content)

        # Check the post text is in the response
        self.assertTrue(bytes(post.text, 'utf-8') in response.content)

        # Check the post date is in the response
        self.assertTrue(bytes(str(post.pub_date.year), 'utf-8') in response.content)
        self.assertTrue(bytes(post.pub_date.strftime('%b'), 'utf-8') in response.content)
        self.assertTrue(bytes(str(post.pub_date.day), 'utf-8') in response.content)

        # Check the link is marked up properly
        self.assertTrue(bytes('<a href="http://127.0.0.1:8000/">my first blog post</a>', 'utf-8') in response.content)


class FeedTest(LiveServerTestCase):
    def test_all_post_feed(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create a post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.category = category

        # Save it
        post.save()

        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)

        # Fetch the feed
        response = self.client.get('/feeds/posts/')
        self.assertEqual(response.status_code, 200)

        # Parse the feed
        feed = feedparser.parse(response.content)

        # Check length
        self.assertEqual(len(feed.entries), 1)

        # Check post retrieved is the correct one
        feed_post = feed.entries[0]
        self.assertEqual(feed_post.title, post.title)
        self.assertEqual(feed_post.description, post.text)
