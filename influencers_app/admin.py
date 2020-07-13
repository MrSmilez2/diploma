from django.contrib import admin

from influencers_app.models import Influencer
from influencers_app.models import Content
from influencers_app.models import InfluencersInformation
from influencers_app.models import VideoInformation
from influencers_app.models import ArtzProductUS
from influencers_app.models import Shipment

admin.site.register(Influencer)
admin.site.register(Content)
admin.site.register(InfluencersInformation)
admin.site.register(VideoInformation)
admin.site.register(ArtzProductUS)
admin.site.register(Shipment)
