"""
artists.py
----------
Implement the Artist class representing musicians and content creators.

Classes to implement:
  - Artist
"""
class Artist:
    """Represents an artist who creates tracks on the platform

    Attributes:
        artist_id (str): unique identifier 
        name (str): artist name
        genre (str): artist genre
        tracks (list): list of tracks created by the artist
    """

    def __init__(self, artist_id: str, name: str, genre: str):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.tracks = []

    """Add a track to the artist's collection """
    def add_track(self, track) -> None:
        
        self.tracks.append(track)
    
    """Return the number of tracks created by the artist """
    def track_count(self) -> int:
        return len(self.tracks)

    """Compare artists based on their unique artist_id """
    def __eq__(self, other) -> bool:
        if not isinstance(other, Artist):
            return False
        return self.artist_id == other.artist_id