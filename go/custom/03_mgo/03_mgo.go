package _3_mgo

import (
	"fmt"
	"github.com/go-ini/ini"
	"gopkg.in/mgo.v2"
	"gopkg.in/mgo.v2/bson"
	"log"
	"os"
)

type Account struct {
	Id   int64
	Name string
}

func Test() {
	// 加载配置文件
	cfg, err := ini.Load("db.ini")
	if err != nil {
		fmt.Printf("Fail to read file: %v", err)
		os.Exit(1)
	}
	cs := cfg.Section("mongodb")

	// 连接mongodb
	session, err := mgo.Dial(cs.Key("url").String())
	if err != nil {
		panic(err)
	}
	defer session.Close()

	// 集合
	c := session.DB("go").C("accounts")

	// 登录collection
	goDb := session.DB("go")
	err = goDb.Login(cs.Key("user").String(), cs.Key("pwd").String())
	if err != nil {
		panic("认证登陆错误")
	}

	// 插入
	err = c.Insert(
		&Account{1, "caiyina"},
		&Account{2, "huoshangfei"},
	)
	if err != nil {
		log.Fatal(err)
	}

	// 按条件查找
	account := &Account{}
	err = c.Find(bson.M{"name": "huoshangfei"}).One(account)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(account)

	// 所有
	accounts := make([]Account, 100)
	err = c.Find(bson.M{}).All(&accounts)
	fmt.Println(accounts)
}
