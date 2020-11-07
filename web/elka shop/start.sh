#!/usr/bin/env sh

ELK_HOST="${ELK_HOST:-127.0.0.1}"
ELK_PORT="${ELK_PORT:-9200}"

create_index() {
    local name="$1"
    echo "create index $name at $ELK_HOST:$ELK_PORT" >&2
    curl -X PUT "$ELK_HOST:$ELK_PORT/${name}/post/1" -vfs \
    -H 'Content-Type: application/json' \
     -d '{"type":"Сосна обыкновенная","count":"123","price":"600"}'
}

create_flag() {
    echo "create flag index at $ELK_HOST:$ELK_PORT" >&2
    curl -X PUT "$ELK_HOST:$ELK_PORT/flag/post/1" -vfs \
    -H 'Content-Type: application/json' \
     -d '{"flag":"PermCTF{winter_is_coming}"}'
}

check_index() {
    local name="$1"
    curl "$ELK_HOST:$ELK_PORT/${name}" -sf >/dev/null 2>&1
}

get_index() {
    local name="$1"
    curl "$ELK_HOST:$ELK_PORT/${name}/post/1" -sf >/dev/null
}

tcp_port_is_open() {
    local host="$1"
    local port="$2"
    (echo > "/dev/tcp/$host/$port") 2>/dev/null 
}

echo "wait ELK port is open" >&2
while ! tcp_port_is_open "$ELK_HOST" "$ELK_PORT"; do
    echo "..." >&2
    sleep 1
done


echo "init indexes" >&2
while true; do
    if check_index "elka"; then break; fi
    create_index elka || { echo "Cannot create index" >&2; sleep 1; exit 1; }
    create_flag       || { echo "Cannot create index" >&2; sleep 1; exit 1; }
done
echo "done" >&2

INDEX_JSON="$( get_index elka )" 2>/dev/null || { echo error; exit 1; }
echo -e "index elka:\n$INDEX_JSON"
