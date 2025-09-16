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


"""
Single resposibility principle focuses on a class/service having single responsiblity to perform. For example a User class must perform only user related actions
and NOT email OR phone related methods despite being used by that user

How to identify such cases?

=> Ask why this class will change - Each distinct reason to change means different responbility. If it changes because of business rules AND changes in file formats, it has 2 responsibilties. If it changes bcos of how data is presented AND bcos of how it's stored then 2 again

=> Responsibility types:
    - Business logic - core rules/rule engine
    - data access - DB or file systems
    - presentation logic - UI/reports
    - communication - external service/APIs
    - validation - check user input or data correctness

=> A class with more than 1 description: It handles User registration AND sending login/registration emails

=> testability: check for dependencies, mocks and in general coupling

Idea is to make classes more modular and NOT make lot of tiny classes. Reduce coupling between unrelated behaviours

Example scenario: User Registration System

- Validates user data
- Saves user data in DB
- sends email to user
- auth workflows for user

It can be made as:
- UserValidator: validate user input
- EmailService: manages sending emails
- UserRepository: Handles DB operations 
- UserRegistrationService: handles registratrion workflows for user


In this way each class is simpler, easy to test, changes localized
"""




