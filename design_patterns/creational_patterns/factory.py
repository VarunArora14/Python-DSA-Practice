"""
It is creational pattern  providing interface for creating objects in a superclass, but allows subclasses to alter type of objects to be created.

Use cases:
- exact type unknown in runtime
- object creation is complex, repetitive or needs encapsulation
- you want open/closed principle being followed

Imagine you have EmailNotification class and have NotificationService that sends notification. Now, if the mobile notifications add up,
you have to either modify the notification service each time with if-else statements based on "type" being passed to notification service
to determine which is the methods of which class to be called. That if-else can get bigger and more complex if dependencies not injected
as well in them.

It hides object creation logic, decouples code as client code does not need to know which class is being instantiated
"""

from abc import ABC, abstractmethod


# Implement interfaces and open/closed principle first with creating of below Interfaces and then Concrete Implementations

class Notification(ABC):
    @abstractmethod
    def notify(self, message:str):
        pass

class EmailNotification(Notification):
    def notify(self, message:str):
        print(f"Sending email: {message}")

class SMSNotification(Notification):
    def notify(self, message:str):
        print(f"Sending sms: {message}")


# Create the factory class
class NotificationFactory:
    @staticmethod
    def get_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Client Code
def send_alert(notification_type:str, message:str):
    notification_client = NotificationFactory.get_notification(notification_type=notification_type)
    notification_client.notify(message=message)

# Send different types of notifications
send_alert("email", "Server is down!")
send_alert("sms", "New login detected.")
send_alert("push", "You have a new message.")