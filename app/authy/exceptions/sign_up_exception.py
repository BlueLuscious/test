from app.exceptions.custom_exception import CustomException

class SignUpError(CustomException):

    def __init__(self, message, log, code = None, redirect = None) -> None:
        super().__init__(message, log, code, redirect)


class UserAlreadyExistError(CustomException):

    def __init__(self, log) -> None:
        super().__init__(
            log,
            message="This username already exists",
            code="UserAlreadyExistError",
            redirect="sign-up"
        )


class PasswordLengthError(CustomException):

    def __init__(self, log) -> None:
        super().__init__(
            log,
            message="Password must have between 6 and 12 characters",
            code="PasswordLengthError",
            redirect="sign-up"
        )
