import nmap

# de unde pana unde scanez porturile IP-ului
begin = 75
end = 80


target = '192.168.0.1'

# folosesc nmap
scanner = nmap.PortScanner()

for i in range(begin, end + 1):
    res = scanner.scan(target, str(i))

    # acesam dictionarul (key-value pairs)
    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}.')
