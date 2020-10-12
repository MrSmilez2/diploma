from django.contrib import admin

from influencers_app.models import (
    Influencer,
    Content,
    InfluencersInformation,
    VideoInformation,
    ArtzProductUS,
    Shipment,
    Book,
)


admin.site.register(Influencer)
admin.site.register(Content)
admin.site.register(InfluencersInformation)
admin.site.register(VideoInformation)
admin.site.register(ArtzProductUS)
admin.site.register(Shipment)
admin.site.register(Book)
