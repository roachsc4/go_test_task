import sys

args = sys.argv
if len(args) != 2:
    print('Запустите скрипт, указав один файл.')
filename = args[1]
line_counter = 0
try:
    with open(filename, 'r') as f:
        for line in f:
            line_counter += 1
except OSError as e:
    if e.errno == 2:
        print("Файл %s не найден." % filename)
    else:
        print('Непредвиденная ошибка во время работы с файлом.')
    sys.exit()
f.close()
print(filename, line_counter)




