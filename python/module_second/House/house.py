

class House:
  def __init__(self):
    self.num_rooms=4
    self.address={
      "number":1,
      "street_name":"A street",
      "zip_code":"22222"
    }
    self.lights=False
    
    def getAddress(self):
      return self.address
    def getNumRooms(self):
      return self.num_rooms
    def turn_on(self):
      self.lights=True
    def turn_off(self):
      self.lights=False