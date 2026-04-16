"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from datetime import datetime, timedelta
from streaming.users import User,PremiumUser,FamilyAccountUser
from streaming.tracks import Track, Song
from streaming.artists import Artist
from streaming.albums import Album
from streaming.playlists import Playlist, CollaborativePlaylist
from streaming.sessions import ListeningSession

class StreamingPlatform:
  
    """Central class managing all entities in the streaming platform 

    Responsible for:
        - storing users, tracks, artists, albums, playlists
        - recording listening sessions
        - providing analytics queries (Q1 - Q10)
    """
    
    def __init__(self,name:str):
      
      self.name = name
      self._catalogue:dict[str,Track] = {}
      self._users:dict[str,User] = {}
      self._artists:dict[str,Artist] = {}
      self._albums:dict[str,Album] = {}
      self._playlists:dict[str,Playlist] = {}
      self._sessions: list[ListeningSession] = []
      
    def add_track(self,track:Track) -> None:
      """Add a track to the platform catalogue """
      self._catalogue[track.track_id] = track
    
    def add_user(self,user:User) -> None:
      """Add a user to the platform catalogue """
      self._users[user.user_id] = user
    
    def add_artist(self,artist:Artist) -> None:
      """Add a artist to the platform catalogue """
      self._artists[artist.artist_id] = artist
    
    def add_album(self,album:Album) ->None:
      """Add a album to the platform catalogue """
      self._albums[album.album_id] = album
    
    def add_playlist(self,playlist:Playlist) -> None:
      """Add a playlist to the platform catalogue """
      self._playlists[playlist.playlist_id] = playlist
    
    def  record_session(self,session:ListeningSession) -> None:
      """Record a listening session and link it to the user  """
      self._sessions.append(session)
      session.user.add_session(session)
      
    def get_track(self, track_id:str) -> Track | None:
      """Return a track by ID or None if not found """
      return self._catalogue.get(track_id)
    
    def get_user(self,user_id:str) ->User | None:
      """Return a user by ID or None if not found """
      return self._users.get(user_id)
    
    def get_artist(self,artist_id:str) -> Artist | None:
      """Return an artist by ID or None if not found """
      return self._artists.get(artist_id)
    
    def get_album(self,album_id:str) -> Album | None:
      """Return an album by ID or None if not found """
      return self._albums.get(album_id)
    
    def all_users(self) -> list[User]:
      """Return a list of all users on the platform """
      return list(self._users.values())
    
    def all_tracks(self) -> list[Track]:
      """Return a list of all tracks on the platform """
      return list(self._catalogue.values())
    
  
      
      
      
      
    def total_listening_time_minutes(self,start: datetime, end: datetime) -> float:
          """Return total listening time in minutes within a time window """
          total_seconds = 0
          
          for session in self._sessions:
            if start <= session.timestamp <= end:
              total_seconds += session.duration_listened_seconds
          return total_seconds / 60
        
    def avg_unique_tracks_per_premium_user(self,days:int = 30) -> float:
      """Return average number of unique tracks listened to by PremiumUsers
      in the last given number of days 
    
      Returns 0  if there are no premium users 
    """
      now = datetime.now() - timedelta(days=days)
      
      
      premium_users = [user for user in self._users.values() if isinstance(user,PremiumUser)]
      
      if not premium_users:
        return 0.0 
      
    
      
      total_unique_tracks = 0
      
      for user in premium_users:
        unique_tracks = set()
        for session in user.sessions:
          if session.timestamp >= now:
            unique_tracks.add(session.track.track_id)
            
        total_unique_tracks += len(unique_tracks)
        
      return total_unique_tracks / len(premium_users)
      
      
    def track_with_most_distinct_listeners(self) -> Track | None:
      """Return the track listened to by the highest number of unique users """
      if not self._sessions:
        return None
      
      track_users = {}
      
      for session in self._sessions:
        track_id = session.track.track_id
        user_id = session.user.user_id
        
        if track_id not in track_users:
          track_users[track_id] = set()
        track_users[track_id].add(user_id)
          
      max_track_id = None
      max_count = 0
        
      for track_id,user_ids in track_users.items():
        if len(user_ids) > max_count:
          max_count = len(user_ids)
          max_track_id = track_id
      if max_track_id is None:
        return None
          
      return self.get_track(max_track_id)
    
    def  avg_session_duration_by_user_type(self) -> list[tuple[str,float]]:
      """Return average session duration per user type, sorted descending """
      stats = {}
      
      for session in self._sessions:
        
        user_type = type(session.user).__name__
        
        if user_type not in stats:
          stats[user_type] = {"total": 0, "count" : 0}
          
        stats[user_type]["total"] += session.duration_listened_seconds
        stats[user_type]["count"] += 1
      result = []
      for user,data in stats.items():
        avg = data["total"] / data["count"]
        result.append((user,avg))
      result.sort(key= lambda x:x[1], reverse = True)
      
      return result
    
    def total_listening_time_underage_sub_users_minutes(self,age_threshold: int = 18) -> float:
      """Return total listening time in min  for family sub-users under given age """
      total_seconds = 0
      for user in self._users.values():
        if isinstance(user,FamilyAccountUser):
          for sub_user in user.sub_users:
            if sub_user.age < age_threshold:
              total_seconds += sub_user.total_listening_seconds()
              
      return total_seconds / 60 

    def top_artists_by_listening_time(self,n : int = 5) -> list[tuple[Artist,float]]:
      """Return top n artists ranked by listening time in min """
      top_artists = {}
      
      for session in self._sessions:
        
        track = session.track
        if not isinstance(track,Song):
          continue
        
        artist_id = track.artist.artist_id
        
        if artist_id not in top_artists:
          top_artists[artist_id] = 0
          
        top_artists[artist_id] += session.duration_listened_seconds
      result = []
      
      for artist_id, total_seconds in top_artists.items():
        artist = self.get_artist(artist_id)
        result.append((artist,total_seconds / 60))
        
      result.sort(key = lambda x: x[1], reverse = True)
      return result[:n]
        # def top_artists_by_listening_time(self, n : int = 5) -> list[tuple[Artist,float]]:
      
     

    def user_top_genre(self,user_id:str) -> tuple[str,float] | None:
      """Return user's most listened genre and its percentage of total listening time """
      
      user = self.get_user(user_id)
      
      if not user:
        return None
      
      genre_time = {}
      total_time = 0
      
      for session in user.sessions:
        genre = session.track.genre
        if genre not in genre_time:
          genre_time[genre]= 0
        genre_time[genre] += session.duration_listened_seconds
        total_time  += session.duration_listened_seconds
        
      if total_time == 0:
        return None
        
      top_genre = max(genre_time,key=lambda g: genre_time[g])
      percentage = (genre_time[top_genre] / total_time) * 100
      
      return (top_genre,percentage)
    
    def collaborative_playlists_with_many_artists(self, threshold: int = 3) -> list[CollaborativePlaylist]:
      
      """Return collaborative playlists with more than threshold distinct artists """
      
      result = []
      for playlist in self._playlists.values():
        if not isinstance(playlist,CollaborativePlaylist):
          continue
          
        artists = set()
        
        for track in playlist.tracks:
          if isinstance(track,Song):
            artists.add(track.artist.artist_id)
        if len(artists) > threshold:
          result.append(playlist)
            
      return result
        
       
    def avg_tracks_per_playlist_type(self) -> dict[str,float]:
      
      """Return average number of tracks per playlist type """

      playlist_total  = 0 
      playlist_count = 0
      
      collaborative_total = 0 
      collaborative_count = 0 
      
      for playlist in self._playlists.values():
        
        if isinstance(playlist,CollaborativePlaylist):
          collaborative_total += len(playlist.tracks)
          collaborative_count += 1        
        else:
          playlist_total += len(playlist.tracks)
          playlist_count += 1
    
      
      playlist_avg = playlist_total / playlist_count if playlist_count>0 else 0.0
      collaborative_avg = collaborative_total / collaborative_count if collaborative_count > 0 else 0.0
          
      result = {}
      
      result["Playlist"] = playlist_avg
      result["CollaborativePlaylist"] = collaborative_avg
      
      return result
      
      
      
    def users_who_completed_albums(self) -> list[tuple[User,list[str]]]:
      
      """Return users who listened to all tracks of at least one album """
      
      result = []
      
      for user in self.all_users():
        user_track_ids = user.unique_tracks_listened()
        
        completed_albums = []
        for album in self._albums.values():
          album_track_ids = album.track_ids()
          
          if not album_track_ids:
            continue
          if album_track_ids.issubset(user_track_ids):
            completed_albums.append(album.title)
        if completed_albums:
          result.append((user, completed_albums))
            
      return result
       

    