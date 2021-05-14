
def ip2bin(ip):
  nums = ip.split(".")
  nums = list(map(lambda x: int(x), nums))
  total = (nums[0]<<24) + (nums[1]<<16) + (nums[2]<<8) + nums[3]
  return total

def bin2ip(num):
  nums = [0, 0, 0, 0]
  nums[0] = (num & 0b11111111000000000000000000000000)>>24
  nums[1] = (num & 0b00000000111111110000000000000000)>>16
  nums[2] = (num & 0b00000000000000001111111100000000)>>8
  nums[3] = num & 0b00000000000000000000000011111111
  return "{:0d}.{:0d}.{:0d}.{:0d}".format(nums[0], nums[1], nums[2], nums[3])

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n