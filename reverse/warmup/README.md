# Описание
Службой КГБ был перехвачен шифр и программа шифрования от наших капиталистических соперников. Товарищ Майор просит вашей помощи в расшифровке файлов.
# Файлы

flag
flag_enc
warmup.py
warmup.pyc


# Файлы для участников

flag_enc
warmup.pyc

# Решение
uncompyle6 warmup.pyc
Видим
```
try:
    if int(sys.argv[1]) == 3735928559:
      print('BACKDOOR')
      print('pumr4w_ftcmrep'[::-1])
```
Создаем файл с названием 3735928559 или переворачиваем строку
Получаем permctf_w4rmup
