from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(
            username='ahmed', password='123'
        )
        testuser1.save()

        testpost = Post.objects.create(
            author = testuser1, title = 'blog title', body = 'body'
        )
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'ahmed')
        self.assertEqual(title, 'blog title')
        self.assertEqual(body, 'body')