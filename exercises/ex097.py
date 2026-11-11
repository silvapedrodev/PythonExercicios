def write(msg):
    size = len(msg) + 4
    print('~' * size)
    print(f'  {msg}')
    print('~' * size)


write('Dev')
write('Curso de Python YouTube')
write('Curso em Video')
