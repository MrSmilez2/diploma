from influencers_app.enums import ContentType, ProgressType


CONTENT_TYPES_MAPPING = (
    (ContentType.YOUTUBE_VIDEO, "Youtube video"),
    (ContentType.TIKTOK_VIDEO, "Tiktok video"),
    (ContentType.INSTAGRAM_POST, "Instagram post"),
)


PROGRESS_TYPES_MAPPING = (
    (ProgressType.REVIEW_DONE, "Review is done"),
    (ProgressType.AWAITING_REVIEW, "Waiting for review to be done"),
    (ProgressType.PRODUCTS_SENT, "Products are sent"),
    (ProgressType.COMMUNICATING, "Communicating is in progress"),
    (ProgressType.OFFER_DECLINED, "Offer is declined"),
    (ProgressType.REJECTION, "Rejection"),
    (ProgressType.EMAIL_INQUIRY_SENT, "Email inquiry is sent"),
    (ProgressType.ON_HOLD, "On hold"),
)
