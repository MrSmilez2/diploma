from django.utils.translation import gettext_lazy as _
from enum import IntEnum


class ProgressType(IntEnum):

    REVIEW_DONE = 1
    AWAITING_REVIEW = 2
    PRODUCTS_SENT = 3
    COMMUNICATING = 4
    OFFER_DECLINED = 5
    REJECTION = 6
    EMAIL_INQUIRY_SENT = 7
    ON_HOLD = 8
    DEFAULT_VALUE = 9

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
