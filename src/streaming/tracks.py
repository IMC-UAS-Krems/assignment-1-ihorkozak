"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
  - Track (abstract base class)
    - Song
      - SingleRelease
      - AlbumTrack
    - Podcast
      - InterviewEpisode
      - NarrativeEpisode
    - AudiobookTrack
"""
from abc import ABC 
from datetime import date

class Track(ABC):
  
  """Base class for all playable content (songs, podcasts, audiobooks)

    Attributes:
        track_id (str): unique identifier
        title (str): Track title
        duration_seconds (int): duration  (seconds)
        genre (str): tracks's genre 
    """
    
  def __init__(self,track_id:str , title:str, duration_seconds:int,genre:str):
    self.track_id = track_id
    self.title = title
    self.duration_seconds = duration_seconds
    self.genre = genre
   
   
  
  """Return track duration in minutes.""" 
  def duration_minutes(self):
    return self.duration_seconds / 60
  
  
  """Compare tracks by their track_id."""
  def __eq__(self, other):
    if not isinstance(other, Track):
      return False
    return self.track_id == other.track_id

class Song(Track):
  """Represents a musical track.

    Attributes:
        artist: Artist 
    """
    
  def __init__(self,track_id:str, title:str, duration_seconds:int, genre:str, artist):
    super().__init__(track_id,title,duration_seconds,genre)
    
    self.artist = artist
    
  
    
class SingleRelease(Song):
  
  """Represents a standalone song released as a single.

    Attributes:
        release_date (date): release date of the song
    """

  def __init__(self, track_id:str, title:str, duration_seconds:int, genre:str, artist, release_date:date):
    super().__init__(track_id,title,duration_seconds,genre,artist)
    self.release_date = release_date
  
   
  
class AlbumTrack(Song):
  
  """Represents a song that belongs to an album.

    Attributes:
        track_number (int): position of the track 
        album: Album reference 
    """
    
  def __init__ (self, track_id:str, title:str,duration_seconds:int, genre:str,artist,track_number:int, album=None,):
    super().__init__(track_id,title,duration_seconds,genre,artist)
    self.track_number = track_number
    self.album = album
    
  
  
class Podcast(Track):
  
  """Represents a podcast episode.

    Attributes:
        host (str): podcast host
        description (str): episode description
    """
    
  def __init__(self,track_id:str, title:str, duration_seconds:int,genre:str, host:str,description:str = ""):
    super().__init__(track_id,title,duration_seconds,genre)
    self.host = host
    self.description = description


class InterviewEpisode(Podcast):
  
  """Podcast episode with a guest interview.

    Attributes:
        guest (str):  guest
    """
    
  def __init__(self, track_id:str, title:str, duration_seconds:int, genre:str, host:str,guest:str, description:str="",):
    super().__init__(track_id,title,duration_seconds,genre,host,description)
    self.guest = guest

  
class NarrativeEpisode(Podcast):
  
  """Podcast episode that is part of a series.

    Attributes:
        season (int): season number
        episode_number (int): episode number
    """

  def __init__(self, track_id:str, title:str, duration_seconds:int, genre:str, host:str, season:int, episode_number:int, description:str = ""):
    super().__init__(track_id,title,duration_seconds,genre,host,description)
    self.season = season
    self.episode_number = episode_number

 

class AudiobookTrack(Track):
  
  
  def __init__(self, track_id:str, title:str, duration_seconds:int, genre:str, author:str, narrator:str):
    super().__init__(track_id,title,duration_seconds,genre)
    self.author = author
    self.narrator = narrator

"""Represents an audiobook segment.

    Attributes:
        author (str): book author
        narrator (str): narrator
    """
 
