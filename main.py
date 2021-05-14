import math
from ip_methods import ip2bin, bin2ip, bit_not
from ip_classes import Network, Mask, LAN


NET_ADDRESS = "212.13.14.0"
NET_MASK = Mask("/24")

LANs = [
  LAN(0, "LAN A", 200),
  LAN(1, "LAN B", 200),
  LAN(2, "LAN C", 200)
]

WANs = [
  (0,1),
  (0,2)
]

TOTAL_SUBNETS = len(LANs) + len(WANs) - 3
SUBNET_BITS = math.ceil(math.log(TOTAL_SUBNETS, 2))
SUBNET_MASK = Mask("/" + str(NET_MASK.asBits() + SUBNET_BITS))

networks = []
for i in range(0, 2**SUBNET_BITS):
  ip_net = ip2bin(NET_ADDRESS) + (i<<(32-SUBNET_MASK.asBits()))
  networks.append(Network("A", ip_net, SUBNET_MASK, ip_net | bit_not(SUBNET_MASK.asBinary(), 32)))

print("-----------------------------------------------------------")
print("{:<8}  {:<15}  {:<2}  {:<15}  {:<}".format("NAME", "NETWORK ADDRESS", "MASK", "BROADCAST", "HOSTS"))
print("-----------------------------------------------------------")
for net in networks:
  print(net)