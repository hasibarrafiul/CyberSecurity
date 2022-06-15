import socket
class IN:
    IP_MTU = 14
    IP_MTU_DISCOVER = 10
    IP_PMTUDISC_DO = 2


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostName = "103.49.169.150"
Port = 9999
s.connect((hostName, Port))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
MTU_Size = 1475
try:
    s.send(b'#' * 44 * MTU_Size)
except socket.error:
    print('The message did not make it')
    option = getattr(IN, 'IP_MTU', 14)
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, option))
else:
    print('The big message was sent! My network supports really big packets!')