import feedparser
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone

from blogengine import models


class PostTest(TestCase):
    def test_create_category(self):
        # Create the category
        category = models.Category()

        # Add attributes
        category.name = 'python'
        category.description = 'The Python programming language'

        # Save it
        category.save()

        # Check we can find it
        all_categories = models.Category.objects.all()
        self.assertEqual(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEqual(only_category, category)

        # Check attributes
        self.assertEqual(only_category.name, 'python')
        self.assertEqual(only_category.description, 'The Python programming language')

    def test_create_tag(self):
        # Create the tag
        tag = models.Tag()

        # Add attributes
        tag.name = 'python'
        tag.description = 'The Python programming language'

        # Save it
        tag.save()

        # Check we can find it
        all_tags = models.Tag.objects.all()
        self.assertEqual(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEqual(only_tag, tag)

        # Check attributes
        self.assertEqual(only_tag.name, 'python')
        self.assertEqual(only_tag.description, 'The Python programming language')

    def test_create_post(self):
        # Create the category
        category = models.Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # create the tag
        tag = models.Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the post
        post = models.Post()

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
        all_posts = models.Post.objects.all()
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

    def test_get_introduction(self):
        # Create the post
        post = models.Post()
        # Add the text to the post
        post.text = "<p>This is my first post that is so awesome</p><p>This a second paragraph</p>"
        self.assertEqual(post.get_introduction(), "This is my first post that is so awesome")

    def test_get_post_content(self):
        # Create the post
        post = models.Post()
        # Add the text to the post
        post.text = "<p>This is my first post that is so awesome</p><p>This a second paragraph</p>"
        self.assertEqual(post.get_text_content(), "<p>This a second paragraph</p>")


class PostViewTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # Create the category
        category = models.Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = models.Tag()
        tag.name = 'perl'
        tag.description = 'The Perl programming language'
        tag.save()

        # Create the post
        post = models.Post()
        post.title = "My first post !!"
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()

        # Check post saved
        all_posts = models.Post.objects.all()
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
        category = models.Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = models.Tag()
        tag.name = 'perl'
        tag.description = 'The Perl programming language'
        tag.save()

        # Create the post
        post = models.Post()
        post.title = 'My first post'
        post.text = '<p>Intro</p><p>This is <a href="http://127.0.0.1:8000/">my first blog post</a></p>'
        post.pub_date = timezone.now()
        post.slug = 'my-first-post'
        post.category = category
        post.save()
        post.tags.add(tag)
        post.save()

        # Check new post saved
        all_posts = models.Post.objects.all()
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
        # Check the post introduction is in the response
        self.assertTrue(bytes(post.get_introduction(), 'utf-8') in response.content)
        # Check the post content is in the response
        self.assertTrue(bytes(post.get_text_content(), 'utf-8') in response.content)
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
        category = models.Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the post
        post = models.Post()
        post.title = 'My first post'
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.category = category
        post.save()

        # Check new post saved
        all_posts = models.Post.objects.all()
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
        self.assertTrue(bytes(category.description, 'utf-8') in response.content)

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
        tag = models.Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the category
        category = models.Category()
        category.name = 'perl'
        category.description = 'The Perl programming language'
        category.save()


        # Create the post
        post = models.Post()
        post.title = 'My first post'
        post.text = 'This is <a href="http://127.0.0.1:8000/">my first blog post</a>'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.category = category
        post.save()

        post.tags.add(tag)
        post.save()

        # Check new post saved
        all_posts = models.Post.objects.all()
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
        category = models.Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create a post
        post = models.Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.category = category

        # Save it
        post.save()

        # Check we can find it
        all_posts = models.Post.objects.all()
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

