class BadSingleResponsibility:
    def authenticate_user(self, username, password):
        # Auth logic
        pass

    def update_user_profile(self, user_id, new_profile_data):
        # profile logic
        pass

    def send_email_notification(self, user_email, message):
        # email logic
        pass

# Below is better implementation of above as each class has it's well-defined responsibility

class UserAuthenticator:
    def authenticate_user(self, username, password):
        pass

class UserProfileManager:
    def update_user_profile(self, user_id, new_profile_data):
        pass

class EmailNotifier:
    def send_email_notification(self, user_email, message):
        # email logic
        pass
