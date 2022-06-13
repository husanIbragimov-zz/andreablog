from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

TYPE = (
    (0, 'FASHION'),
    (1, 'TRAVEL'),
)


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=221)

    def __str__(self):
        return self.tag


# get_<field_name>_display
def post_image_path(instance, filename):
    return 'posts/%s/%s' % (instance.get_type_display(), filename)


class Post(models.Model):
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to=post_image_path)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.title

    def post_comments_count(self):
        return self.comment_set.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='comments', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
