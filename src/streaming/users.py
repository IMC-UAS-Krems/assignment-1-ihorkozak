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
  def __init__(self,user_id:str, name:str, age:int):
    self.user_id = user_id
    self.name = name
    self.age = age
    self.sessions = []
    
  def add_session(self, session) -> None:
    self.sessions.append(session)
  
  def total_listening_seconds(self) -> int:
    return sum(session.duration_listened_seconds for session in self.sessions)

  def total_listening_minutes(self) -> float:
    return self.total_listening_seconds() / 60
  
  def unique_tracks_listened(self) -> set[str]:
    return {session.track.track_id for session in self.sessions}

  def __eq__(self, other) -> bool:
    if not isinstance(other, User):
      return False
    return self.user_id == other.user_id


class FreeUser(User):
  MAX_STEPS_PER_HOURS = 6
  
  def __init__(self,user_id:str, name:str,age:int):
    super().__init__(user_id,name,age)
    
class PremiumUser(User):
  def __init__(self, user_id: str, name: str, age: int, subscription_start:date):
    super().__init__(user_id, name, age)
    self.subscription_start: date = subscription_start
        
class FamilyAccountUser(User):
  def __init__(self,used_id:str, name:str, age:int):
    super().__init__(used_id,name,age)
    self.sub_users = []
  
  def add_sub_user(self,sub_user):
    self.sub_users.append(sub_user)
  
  def all_members(self):
    return [self] + self.sub_users
  
class FamilyMember(User):
  def __init__(self, user_id: str, name: str, age: int, parent: FamilyAccountUser):
    super().__init__(user_id, name, age)
    self.parent = parent 