# 环境要求
# git
# nodejs
# python 3.5

install(){
    pip3 install pipenv -i https://pypi.douban.com/simple

    pipenv install Pipfile
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
}

start(){
    supervisord -c supervisord.conf
    status
}

stop(){
    supervisorctl stop all
    ps aux | grep supervisord | grep -v 'grep' | awk '{print $2}' | xargs kill -9
    status
}

status(){
    supervisorctl status
}

restart(){
    stop
    start
}

case "$1" in
  install)
        install
        ;;
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        restart
        ;;
  status)
        status
        ;;
  *)
        supervisorctl stop all &> /dev/null
        ret=`supervisorctl start $1`
        if [[ $ret =~ "ERROR (no such process)" ]]
        then
            echo $"Usage: sh $0 {start|stop|restart|status|service_name}"
            exit 2
        else
            cp -f $1.nginx.conf /etc/nginx/nginx.conf
            nginx -s reload
            supervisorctl status $1
        fi
esac
