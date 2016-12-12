from registration.forms import RegistrationFormUniqueEmail


class RegistrationFormWithoutUsername(RegistrationFormUniqueEmail):

    def clean_username(self):
        return self.data['email']