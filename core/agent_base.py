# core/agent_base.py

from core.messaging import Message

class AgentBase:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.inbox = []

    def send_message(self, recipient_agent, content, task=None):
        msg = Message(sender=self.name, recipient=recipient_agent.name, content=content, task=task)
        recipient_agent.inbox.append(msg)
        print(f"{msg}")