import uuid

class Todo:
  def __init__(self, title, completed=False, id=None):
    self.id = id or str(uuid.uuid4())
    self.title = title
    self.completed = completed