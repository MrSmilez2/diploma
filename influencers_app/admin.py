from django.contrib import admin

from influencers_app.models import Influencer, Content, InfluencersInformation
admin.site.register(Influencer)
admin.site.register(Content)
admin.site.register(InfluencersInformation)
