from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.db.models.signals import pre_save

from django.utils.text import slugify

from django.utils.translation import ugettext_lazy as _


class Influencer(models.Model):
    name = models.CharField(max_length=45, unique=True)
    slug = models.SlugField(unique=True, null=True)
    channels_url = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)
    responsible = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="responsible",
        default=None,
    )

    def __str__(self):
        return self.name


class InfluencersInformation(models.Model):
    channel_name = models.ForeignKey("Influencer", on_delete=models.CASCADE, null=True)

    class ProgressType(TextChoices):
        REVIEWDONE = "1RD", _("Review done")
        AWAITINGREVIEW = "2AR", _("Awaiting review")
        PRODUCTSSENT = "3PS", _("Product sent")
        COMMUNICATING = "4CM", _("Communicating")
        OFFERDECLINED = "5OD", _("Offer declined")
        REJECTION = "6RJ", _("Rejection")
        EMAILINQUIRYSENT = "7ES", _("Email inquiry sent")
        ONHOLD = "8OH", _("On hold")
        DEFAULTVALUE = "9DV", _("Send your first message")

    progress = models.CharField(
        max_length=3,
        choices=ProgressType.choices,
        default=ProgressType.DEFAULTVALUE,
    )
    location = models.CharField(max_length=20, null=True, blank=True, default=None)
    subscribers = models.IntegerField(null=True, blank=True, default=None)
    date_of_last_email = models.DateField(
        auto_created=True, null=True, blank=True, default=None
    )
    review_notes = models.TextField(null=True, blank=True, default=None)
    number_of_followups = models.IntegerField(null=True, blank=True, default=None)
    permission_for_ads = models.BooleanField(null=True, blank=True, default=None)
    notes = models.TextField(null=True, blank=True, default=None)
    website = models.CharField(
        max_length=45, unique=True, null=True, blank=True, default=None
    )

    def __str__(self):
        return f"{self.channel_name}"


class Content(models.Model):
    class ContentType(TextChoices):
        YOUTUBE_VIDEO = "YV", _("Youtube video")
        TIKTOK_VIDEO = "TV", _("Tiktok video")
        INSTAGRAM_POST = "IP", _("Instagram post")

    type_of_social_media = models.CharField(
        max_length=2, choices=ContentType.choices, default=None
    )
    channel_name = models.ForeignKey("Influencer", on_delete=models.CASCADE, blank=True)
    video_name = models.CharField(max_length=100, unique=True, null=True, blank=True)

    video_url = models.CharField(max_length=100, unique=True, null=True)
    date_of_publication = models.DateField(blank=True)
    number_of_views = models.IntegerField(null=True, blank=True)
    number_of_comments = models.IntegerField(null=True, blank=True)
    number_of_likes = models.IntegerField(null=True, blank=True)
    number_of_dislikes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.channel_name, self.video_name)


class VideoInformation(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    views_count = models.IntegerField(null=True, blank=True)
    comments_count = models.IntegerField(null=True, blank=True)
    likes_count = models.IntegerField(null=True, blank=True)
    dislikes_count = models.IntegerField(null=True, blank=True)


class ArtzProductUS(models.Model):
    sku = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.sku, self.product_name)


class Shipment(models.Model):
    channel_name = models.ForeignKey("Influencer", on_delete=models.CASCADE, null=True)

    class ShipmentStatus(TextChoices):
        NEED_TO_SHIP = "Need to be shipped"
        SHIPPED = "Shipped"

    shipment_status = models.CharField(
        max_length=18,
        choices=ShipmentStatus.choices,
        default=ShipmentStatus.NEED_TO_SHIP,
    )
    product = models.ManyToManyField("ArtzProductUS", related_name="products")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    order_number = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.channel_name, self.created_at)


class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    co_authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="co_authored_by"
    )


def pre_save_influencer_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Influencer.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_influencer_receiver, sender=Influencer)
