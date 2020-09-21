from django.utils.translation import gettext_lazy as _
from enum import IntEnum


class Progress(IntEnum):

    REVIEW_DONE = 1, _('Review done')
    AWAITING_REVIEW = 2, _('Awaiting review')
    PRODUCTS_SENT = 3, _('Products sent')
    COMMUNICATING = 4, _('Communicating')
    OFFER_DECLINED = 5, _('Offer declined')
    REJECTION = 6, _('Rejection')
    EMAIL_INQUIRY_SENT = 7, _('Email inquiry sent')
    ON_HOLD = 8, _('On hold')
    DEFAULT_VALUE = 9, _('Default')

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
