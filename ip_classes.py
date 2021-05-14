from ip_methods import bin2ip

class Network:
  def __init__(self, name, net, subnet_mask, broadcast):
    self.name = name
    self.net = net
    self.subnet_mask = subnet_mask
    self.broadcast = broadcast
    self.hosts = broadcast - net - 1
  
  def __str__(self):
    return "{:<8}  {:<15}  /{:<3}  {:<15}  {:<}".format(self.name, bin2ip(self.net), self.subnet_mask.asBits(), bin2ip(self.broadcast), self.hosts)

class Mask:
  def __init__(self, value):
    try:
      total = ip2bin(value) if ("." in value) else self.num2mask(int(value.replace("/","")))
      self.value = total
    except InputError:
      print("Incorrect initial value for mask")
  
  @staticmethod
  def num2mask(num):
    to_shift = 32 - num
    number = sum([2**i for i in range(num)])
    mask_value = number<<to_shift
    return mask_value

  def asBits(self):
    return bin(self.value).count("1")

  def asBinary(self):
    return self.value

  def __str__(self):
    return bin2ip(int(self.value))

class LAN:
  def __init__(self, id: int, name: str, max_hosts: int):
    self.id = id
    self.name = name
    self.max_hosts = max_hosts
  
  def __str__(self):
    return "<{0}, \"{1}\", MAX={2}>".format(self.id, self.name, self.max_hosts)