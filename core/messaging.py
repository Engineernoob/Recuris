# core/messaging.py

class Message:
    def __init__(self, sender, recipient, content, task=None):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.task = task  # Optional task this message refers to

    def __repr__(self):
        return f"[📩 {self.sender} → {self.recipient}]: {self.content}"