from random import randint

richieste = []
blacklist = [
  '1.25',
  '255.25',
  '1.1',
  '1.8',
  '1.9'
]

def request(ip):
  for blackIp in blacklist:
    if blackIp == ip: 
      return False

  #count = 0
  #for requestedId in richieste:
  #  if requestedId == ip:
  #    count += 1
  #    if count > 3:
  #      blacklist.append(ip)
  #      return False

  if richieste.count(ip) > 3:
    blacklist.append(ip)
    return False

  richieste.append(ip)
  return True  

blockedCounter = 0
requests = 50000
for i in range(requests):
  ip = str(randint(1,255)) + '.' + str(randint(1,255))
  if request(ip) == False:
    print('Blocked request from ip', ip)
    blockedCounter += 1

print('Sono state effettuate', requests, 'requests e ne sono state bloccate', blockedCounter)
print('La blacklist è di', len(blacklist),'ip:')
for ip in blacklist:
  print(ip)