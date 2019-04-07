package _4_go_redis

import (
	"fmt"
	"github.com/go-ini/ini"
	"github.com/go-redis/redis"
	"os"
)

func Test() {
	// 加载配置文件
	cfg, err := ini.Load("db.ini")
	if err != nil {
		fmt.Printf("Fail to read file: %v", err)
		os.Exit(1)
	}
	cs := cfg.Section("redis")

	// 初始化
	dbNum, _ := cs.Key("db").Int()
	client := redis.NewClient(&redis.Options{
		Addr:     cs.Key("url").String(),
		Password: cs.Key("pwd").String(),
		DB:       dbNum,
	})

	// Ping
	pong, err := client.Ping().Result()
	fmt.Println(pong, err)

	// Set
	err = client.Set("key1", "hhhcccc", 0).Err()
	if err != nil {
		panic(err)
	}

	// Get
	val, err := client.Get("key1").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("key1", val)

	// not found
	val2, err := client.Get("key2").Result()
	if err == redis.Nil {
		fmt.Println("key2 does not exist")
	} else if err != nil {
		panic(err)
	} else {
		fmt.Println("key2", val2)
	}

	// HM
	kv := make(map[string]interface{}, 50)
	kv["11"] = "aa"
	kv["22"] = "bb"
	kv["33"] = "cc"
	_, err = client.HMSet("key3", kv).Result()
	val3, err := client.HMGet("key3", "22", "11").Result()
	fmt.Println(val3)
}
