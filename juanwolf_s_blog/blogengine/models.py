from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from juanwolf_s_blog.settings import MEDIA_URL


def upload_path(self, filename):
    import time
    return '%s_%s' % (time.strftime("%Y%m%d_%H%M%S"), filename)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super(Tag, self).save()

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super(Category, self).save()

    def get_absolute_url(self):
        url = "/%s/" % self.slug
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('categories')


class Post(models.Model):
    pub_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, default="")
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    title = models.CharField(max_length=200, default="")
    text = models.TextField(default="")
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def get_absolute_image_url(self):
        return 'http://%s%s%s' % (Site.objects.get_current().domain, MEDIA_URL, self.image.name)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    i18n = True

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
