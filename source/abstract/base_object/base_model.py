#import pygame
import math, uuid
from datetime import datetime, timedelta

class BaseModel:
    uuid = None
    created = None
    parent = None

    def __init__(self, parent):
        self.parent = parent
        self.uuid = uuid.uuid4()
        self.created = datetime.now()
        pass

    def created_delta(self):
        return (datetime.now() - self.created).total_seconds()
