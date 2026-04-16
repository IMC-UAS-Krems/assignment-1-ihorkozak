"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""


from datetime import date

class User:
  
  """Base class for all platform users

    Attributes:
        user_id (str): unique identifier 
        name (str): user name
        age (int): user age
        sessions (list): listening sessions associated with the user
    """
    
  def __init__(self,user_id:str, name:str, age:int):
    self.user_id = user_id
    self.name = name
    self.age = age
    self.sessions = []
    
  def add_session(self, session) -> None:
    """Add a listening session to the user """
    self.sessions.append(session)
  
  def total_listening_seconds(self) -> int:
    """Return the total listening time in seconds """
    return sum(session.duration_listened_seconds for session in self.sessions)

  def total_listening_minutes(self) -> float:
    """Return the total listening time in minutes """
    return self.total_listening_seconds() / 60
  
  def unique_tracks_listened(self) -> set[str]:
    """Return a set of unique track IDs listened to by the user """
    
    return {session.track.track_id for session in self.sessions}

  def __eq__(self, other) -> bool:
    """Compare users by their unique user_id """
    
    if not isinstance(other, User):
      return False
    return self.user_id == other.user_id


class FreeUser(User):
  """Represents a free-tier platform user """
  MAX_STEPS_PER_HOURS = 6
  
  def __init__(self,user_id:str, name:str,age:int):
    super().__init__(user_id,name,age)
    
class PremiumUser(User):
  
  """Represents a premium platform user.

    Attributes:
        subscription_start (date): subscription start date
        
        v
    """
    
  def __init__(self, user_id: str, name: str, age: int, subscription_start:date):
    super().__init__(user_id, name, age)
    self.subscription_start: date = subscription_start
        
class FamilyAccountUser(User):
  
  """Represents the main owner of a family account 

    Attributes:
        sub_users (list): FamilyMember users linked to this account
        
    """
    
  def __init__(self,used_id:str, name:str, age:int):
    super().__init__(used_id,name,age)
    self.sub_users = []
  
  def add_sub_user(self,sub_user):
    """Add a family member to this family account """
    self.sub_users.append(sub_user)
  
  def all_members(self):
    """Return the account owner and all linked sub-users """
    return [self] + self.sub_users
  
class FamilyMember(User):
  """Represents a sub-user in a family account 

    Attributes:
        parent (FamilyAccountUser): parent family account owner
        
    """
    
  def __init__(self, user_id: str, name: str, age: int, parent: FamilyAccountUser):
    super().__init__(user_id, name, age)
    self.parent = parent 