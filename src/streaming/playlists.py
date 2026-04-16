"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""
from streaming.users import User
class Playlist:
  
    """Represents a collection of tracks created by a user

    Attributes:
    
        playlist_id (str): unique identifier 
        name (str): playlist name
        owner (User): user who owns the playlist
        tracks (list): list of tracks in the playlist
        
    """
    
    def __init__(self, playlist_id:str, name:str, owner:User):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner 
        self.tracks = []
        
    def add_track(self,track) -> None:
      """Add a track to the playlist if it is not already present """
      
      
      if track not in self.tracks:
        self.tracks.append(track)
    def remove_track(self,track_id) -> None:
      
        """Remove a track from the playlist by its ID  """
      
        self.tracks = [track for track in self.tracks if track.track_id != track_id]
    
    def total_duration_seconds(self) -> int:

        """Return the total duration of all tracks in seconds """
        
        return sum(track.duration_seconds for track in self.tracks)
    
    def __eq__(self, other) -> bool:
      
        """Compare playlists by their unique playlist_id """
      
        if not isinstance(other, Playlist):
            return False
        return self.playlist_id == other.playlist_id
    
class CollaborativePlaylist(Playlist):
    """Represents a playlist that can be edited by multiple users 

    Attributes:
    
        contributors (list): ussers who can modify the playlist
        
    """
    
    def __init__(self,playlist_id:str,name:str, owner:User):
      super().__init__(playlist_id,name,owner)
      self.contributors = [owner]
    def add_contributor(self,user) -> None:
      """Add a contributor to the playlist """
      
      if user not in self.contributors:
        self.contributors.append(user)
    
    def remove_contributor(self,user) -> None:
      
      """Remove a contributor from the playlist  """
      
      if user == self.owner:
        return
      self.contributors = [contributor for contributor in self.contributors if contributor != user]
        
      
    
      
