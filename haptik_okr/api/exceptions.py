class APIError(Exception):
    def __init__(self, message, status):
        """
        Exception raised to handle API error responses

        Args:
            message (str): error message to be returned in the API response
            status (int): valid HTTP status code e.g. 400
        """
        self.message = message
        self.status = status

    def __str__(self):
        return self.message
