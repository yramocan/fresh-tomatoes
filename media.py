class Movie(object):
    # Constructor for Movie Class
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 release_date, director, screenwriter):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
        self.director = director
        self.screenwriter = screenwriter
