class Api:
  def Sensor(self, values):
    device = values.get('device')
    value  = values.get('value')
    if not device or not value: return

    self.values.addValue(device, 'humidity', value)
    self.values.addValue(device, 'device', device)