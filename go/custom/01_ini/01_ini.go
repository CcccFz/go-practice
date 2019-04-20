package _1_ini

import (
	"fmt"
	"github.com/go-ini/ini"
	"os"
)

func Test() {
	cfg, err := ini.Load("db.ini")

	if err != nil {
		fmt.Printf("Fail to read file: %v", err)
		os.Exit(1)
	}

	// read
	fmt.Printf("get value: %s\n", cfg.Section("mongodb").Key("pwd").String())

	// write
	cfg.Section("path").Key("name").SetValue("lxf")
	cfg.SaveTo("db.ini")
}
