d0 = int(input().split()[1])
h0, m0, s0 = map(int, input().split(' : '))
df = int(input().split()[1])
hf, mf, sf = map(int, input().split(' : '))

s, m, h, d = 0, 0, 0, 0
if sf>=s0: 
    s = sf-s0
else:
    s = 60-abs(sf-s0)
    m = -1

if mf>=m0:
    m += mf-m0
else:
    m += 60-abs(mf-m0)
    h = -1

if hf>=h0:
    h += hf-h0
else: 
    h += 24-abs(hf-h0)
    d = -1
    
if m == -1:
    h -= 1
    m = 59
elif h == -1:
    d -= 1
    h = 23
    
d += df - d0
print(f'{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)')