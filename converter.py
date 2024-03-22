'''
Program zamienia pliki z punktami
w formacie obslugiwanym przez edytor
na pliki w formacie opisanym w zadaniu 8.7
'''

PATH = 'good_points.txt'
M = 5

xs = []
ys = []
ts = []
us = []

with open(PATH, 'r') as file:
    data = (line.rstrip() for line in file.readlines())

xs_group = []
ys_group = []

for line in data:
    if line == ';':
        xs.append(xs_group)
        ys.append(ys_group)
        ts.append([k / len(xs_group) for k in range(len(xs_group))])
        us.append([k / M for k in range(M)])
        xs_group = []
        ys_group = []
    else:
        cords = line.split(',')
        xs_group.append(cords[0])
        ys_group.append(cords[1])

def save(path, list):
    with open(path, 'w') as file:
        for group in list:
            for value in group:
                file.write(f'{value}\n')
            file.write('\n')

save('x.txt', xs)
save('y.txt', ys)
save('t.txt', ts)
save('u.txt', us)