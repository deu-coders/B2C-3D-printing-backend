from allauth.account.adapter import DefaultAccountAdapter

# https://stackoverflow.com/questions/37841612/django-rest-auth-custom-registration-fails-to-save-extra-fields
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        # user_field(user, 'gender', request.data.get('gender', ''))
        # user_field(user, 'date_of_birth', request.data.get('date_of_birth', ''))
        user_field(user, 'name', request.data.get('name', ''))
        user_field(user, 'phone', request.data.get('phone', ''))
        user_field(user, 'address', request.data.get('address', ''))

        user.save()
        return user