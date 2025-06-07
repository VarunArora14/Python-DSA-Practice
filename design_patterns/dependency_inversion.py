from abc import ABC, abstractmethod

# class GmailClient:
#     def send_email(self, recepient, subject, body):
#         pass
#
# class EmailService:
#     def __init__(self):
#         self.gmail_client = GmailClient()
#     def send_email(self, recepient, subject, body):
#         self.gmail_client.send_email(recepient=recepient ,subject=subject, body=body)

# Now the Email Service has dependency on the Gmail Client and it violates Dependency Inverion principle (DIP) as the email service is
# tightly coupled to low level Gmail Client. So we do the following

class EmailClient(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, body):
        raise NotImplementedError

class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        print("Gmail Client invoked!")
        print(f"Email details: recipient={recipient}, subject={subject}, body={body}")

class OutlookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        pass

class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client=  email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

gmail_client = GmailClient()
email_service = EmailService(email_client=gmail_client)
email_service.send_email("recipient@email.com", "subjectd", "body")
