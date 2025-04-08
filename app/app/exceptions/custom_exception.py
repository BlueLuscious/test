class CustomException(Exception):

    """ Base exception for custom exceptions. """

    def __init__(self, log: str, message: str, code: str = None, redirect: str = None) -> None:

        """
        CustomException Initializer.
        
        Args:
            message (str): A message.
            log (str): A log.
            code (str): Exception Code.
            redirect (str): A redirect.

        Returns:
            None: Returns `None`.
        """

        self.message = message
        self.log = log
        self.code = code
        self.redirect = redirect
        super().__init__(message, code, redirect)
