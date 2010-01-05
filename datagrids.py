from reviewboard.reviews.templatetags.reviewtags import render_star


class StarColumn(Column):
    """
    A column used to indicate whether the object is "starred" or watched.
    The star is interactive, allowing the user to star or unstar the object.
    """
    def __init__(self, *args, **kwargs):
        Column.__init__(self, *args, **kwargs)
        self.image_url = settings.MEDIA_URL + "rb/images/star_on.png"
        self.image_width = 16
        self.image_height = 15
        self.image_alt = _("Starred")
        self.detailed_label = _("Starred")
        self.shrink = True

    def render_data(self, obj):
        return render_star(self.datagrid.request.user, obj)
