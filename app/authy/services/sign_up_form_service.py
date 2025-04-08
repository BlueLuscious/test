from authy.forms.sign_up_form import SignUpForm
from authy.exceptions.sign_up_exception import (
    PasswordLengthError,
    UserAlreadyExistError,
)
from client.models.client_model import ClientModel


class SignUpFormService:

    """ Service for Sign Up Form. """

    def __init__(self, form: SignUpForm) -> None:
        
        """
        SignUpFormService Initializer.

        Args:
            form (SignUpForm): Form to validate.
        """

        self.form = form


    def validate_form(self) -> SignUpForm:

        data = self.form.data

        username = self.validate_username(data.get("username"))
        password = self.validate_password(data.get("password"))

        validated_data = self.form if self.form.is_valid() else {}
        return validated_data
            

    def validate_username(self, username: str) -> str:

        """ 
        Username validation.

        Args:
            username (str): Username to validate.

        Returns:
            str: Validated username.
        """

        if ClientModel.objects.filter(username=username).exists():
            raise UserAlreadyExistError(f"Username {username} already exists")
        return username


    def validate_password(self, password: str) -> str:
        
        """ 
        Password validation.

        Args:
            password (str): Password to validate.

        Returns:
            str: Validated password.
        """

        if not (6 < len(password) < 12):
            raise PasswordLengthError(f"Password length is {len(password)}, less than 6 or more than 12")
        return password
    