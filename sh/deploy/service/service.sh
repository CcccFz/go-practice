start(){
    supervisord -c supervisord.conf
    status
}

stop(){
    supervisorctl stop all
    ps aux | grep supervisord | grep -v 'grep' | awk '{print $2}' | xargs kill -9
}

status(){
    supervisorctl status
}

restart(){
    stop
    start
}

case "$1" in
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

