from django.dispatch import receiver
from jangle import signals


@receiver(signals.presence_update)
def user_updated(sender, user, status, **_):
    print(f"User {user} is now {status}")
