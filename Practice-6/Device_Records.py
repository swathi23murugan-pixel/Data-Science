records = [('D01', 'Lab-A', 'READY'), ('D02', 'Lab-B', 'BUSY'), ('D01', 'Lab-C', 'MAINTENANCE')]
devices = {}
for device, location, status in records:
    devices[device] = {'location': location, 'status': status}
print(devices)