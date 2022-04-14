
#!/usr/bin/env bash

declare -r DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
 
start() {
    cd ${DIR}
 
    docker-compose up -d
}
 
stop() {
    cd ${DIR}

    docker-compose stop
}

case $1 in
    start) start;;
    stop) stop;;
    "") start;;
    *) echo "Usage: ./service start|stop"
esac