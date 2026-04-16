"""
sessions.py
-----------
Implement the ListeningSession class for recording listening events.

Classes to implement:
  - ListeningSession
"""
from streaming.tracks import Track
from streaming.users import User
from datetime import date

class ListeningSession:
    """Represents a single listening event on the platform

    Attributes:
    
        session_id (str): unique identifier
        user (User): user who listened to the track
        track (Track): track that was played
        timestamp (date): date when the session occurred
        duration_listened_seconds (int): duration listened in seconds
        
        
    """
    """Initialize a listening session with the given attributes """
    def __init__(self,session_id:str, user:User, track:Track,timestamp:date, duration_listened_seconds:int):
        self.session_id = session_id
        self.user = user
        self.track = track
        self.timestamp = timestamp
        self.duration_listened_seconds = duration_listened_seconds
    def duration_listened_minutes(self) -> float:
        """Return the listening duration in minutes """
        return self.duration_listened_seconds / 60