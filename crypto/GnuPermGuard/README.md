# GorodPermGuard
## Описание:
Шифропанки? Не не слышал.
## Решение:
Генерируем PGP ключ, отправляем боту ключ в armored виде. Можно использовать gpg или любое другое приложение. 
`gpg --export --armor <keyid>`

## Флаг 
PermCTF{everybody_needs_encryption}
