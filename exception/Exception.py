class ServiceException(Exception):
    def __init__(self, message="An unknown exception occurred during the service"):
        super().__init__(message)