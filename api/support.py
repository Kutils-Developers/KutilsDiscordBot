class APIError(Exception):
    """
    Base level API Error
    """

    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
