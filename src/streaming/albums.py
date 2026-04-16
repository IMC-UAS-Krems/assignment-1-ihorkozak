"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
from streaming.artists import Artist
class Album:
  
    """Represents a music album consisting of multiple tracks

      Attributes:
        album_id (str): unique identifier 
        title (str): album title
        artist (Artist): artist who created the album
        release_year (int): realse year 
        tracks (list): list of AlbumTrack objects in album 
    """
    
    def __init__(self,album_id:str, title:str,artist:Artist,release_year:int):
      self.album_id = album_id
      self.title = title
      self.artist = artist
      self.release_year = release_year
      self.tracks = []

    def add_track(self,track) -> None:
      """Add a track to the album and maintain track order

        Also assigns this album to the track
        """
      self.tracks.append(track)
      
      track.album = self
      
      self.tracks.sort(key=lambda t: t.track_number)
    
    def track_ids(self) ->set[str]:
      """Return a set of all track IDs in the album """
      return {track.track_id for track in self.tracks}
    
    
    def duration_seconds(self) -> int:
      """Return total duration of all tracks in seconds """
      return sum(track.duration_seconds for track in self.tracks)