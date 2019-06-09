**docker启动postgres实例**
`docker run --name postgres -v ~/data/db/:/var/lib/postgresql/data/ -p 5432:5432 -d mdillon/postgis:latest

**进入容器**
`docker exec -it postgres psql -U postgres -d rental`