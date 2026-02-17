from datetime import datetime
from dataclasses import dataclass

@dataclass
class User:
    name: str
    password: str
    language: str
    enable_notifications: bool
    create_date: datetime
    enabled: bool
    display_name: str