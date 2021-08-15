def APIError(Exception):
    """
    Base level API Error
    attributes:
        level - 
    
    """
    def __init__(self, msg, expr):
        self.msg = msg
        self.expr = expr