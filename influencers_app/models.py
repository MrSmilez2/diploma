from django.db import models
from django.contrib.auth import get_user_model


class Influencer(models.Model):
    name = models.CharField(max_length=45, unique=True)
    channels_url = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50, unique=True)
    responsible = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='responsible',
        default=None
    )

    def __str__(self):
        return self.name


class InfluencersInformation(models.Model):
    channel_name = models.ForeignKey(
        'Influencer',
        on_delete=models.CASCADE,
        null=True
    )
    REVIEWDONE = 'RD'
    AWAITINGREVIEW = 'AR'
    PRODUCTSSENT = 'PS'
    COMMUNICATING = 'CM'
    OFFERDECLINED = 'OD'
    REJECTION = 'RJ'
    EMAILINQUIRYSENT = 'ES'
    ONHOLD = 'OH'
    PROGRESS_CHOICES = [
        (REVIEWDONE, 'Review done'),
        (AWAITINGREVIEW, 'Awaiting review'),
        (PRODUCTSSENT, 'Product sent'),
        (COMMUNICATING, 'Communicating'),
        (OFFERDECLINED, 'Offer declined'),
        (REJECTION, 'Rejection'),
        (EMAILINQUIRYSENT, 'Email inquiry sent'),
        (ONHOLD, 'On hold')
    ]
    location = models.CharField(max_length=20)
    subscribers = models.IntegerField()
    progress = models.CharField(
        max_length=2,
        choices=PROGRESS_CHOICES,
        default=EMAILINQUIRYSENT
    )
    date_of_last_email = models.DateField(auto_created=True, null=True,
                                          blank=True)
    review_notes = models.TextField()
    number_of_followups = models.IntegerField()
    permission_for_ads = models.BooleanField()
    notes = models.TextField()
    website = models.CharField(max_length=45, unique=True)


class Content(models.Model):
    YOUTUBEVIDEO = 'YV'
    TIKTOKVIDEO= 'TV'
    INSTAGRAMPOST = 'IP'
    CONTENT_CHOICES = [
        (YOUTUBEVIDEO, 'Youtube video'),
        (TIKTOKVIDEO, 'Tiktok video'),
        (INSTAGRAMPOST, 'Instagram post')
    ]
    type_of_social_media = models.CharField(
        max_length=2,
        choices=CONTENT_CHOICES,
        default=None
    )
    channel_name = models.ForeignKey(
        'Influencer',
        on_delete=models.CASCADE
    )
    video_name = models.CharField(max_length=100, unique=True, null=True)
    video_url = models.CharField(max_length=100, unique=True, null=True)
    date_of_publication = models.DateField()
    number_of_views = models.IntegerField(null=True, blank=True)
    number_of_comments = models.IntegerField(null=True, blank=True)
    number_of_likes = models.IntegerField(null=True, blank=True)
    number_of_dislikes = models.IntegerField(null=True, blank=True)

    def __str__(self):

        return '{}, {}'.format(self.channel_name, self.video_name)
