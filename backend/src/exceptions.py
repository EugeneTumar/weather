class CountryNotFound(Exception):
    def __init__(self, message="County not found", field=None):
        self.field = field
        super().__init__(message)
