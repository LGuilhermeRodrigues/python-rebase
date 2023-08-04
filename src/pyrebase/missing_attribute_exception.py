class MissingAttributeException(Exception):
  def __init__(self, attribute, *args):
    super().__init__(args)
    self.attribute = attribute

  def __str__(self):
    return f'Essential attribute \'{self.attribute}\' is missing from request'