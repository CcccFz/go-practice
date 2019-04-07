package _2_gorm

import (
	"errors"
	"fmt"
	"github.com/go-ini/ini"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"log"
	"os"
)

type Account struct {
	Id      int64 `gorm:"pk autoincr"`
	Name    string
	Balance float64
	Version int `gorm:"version"`
}

var db *gorm.DB

// 事件钩子
func (account *Account) BeforeCreate() {
	log.Printf("Before Create: %s", account.Name)
}

func (account *Account) AfterCreate() {
	log.Printf("After Create: %s", account.Name)
}

func initDB() {
	// 加载配置文件
	cfg, err := ini.Load("db.ini")
	if err != nil {
		fmt.Printf("Fail to read file: %v", err)
		os.Exit(1)
	}

	// 连接数据库
	db, err = gorm.Open("mysql", cfg.Section("mysql").Key("url").String())
	if err != nil {
		log.Fatalf("Connect DB Failed !!! %v\n", err)
	}

	db.AutoMigrate(&Account{})

	// 日志文件
	f, err := os.OpenFile("sql.log", os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	// 记录日志
	db.LogMode(true)
	db.SetLogger(log.New(f, "\r\n", 0))
}

func getAccountsAsBalance() (accounts []Account, err error) {
	err = db.Order("balance desc").Find(&accounts).Error
	return accounts, err
}

func newAccount(name string, balance float64) error {
	return db.Create(&Account{Name: name, Balance: balance}).Error
}

func getAccount(id int64) (*Account, error) {
	account := &Account{}
	err := db.First(account, id).Error

	if gorm.IsRecordNotFoundError(err) {
		return nil, errors.New("Account not found\n")
	} else if err != nil {
		panic(err)
	}

	return account, nil
}

func makeDeposit(id int64, deposit float64) (*Account, error) {
	account, err := getAccount(id)
	if err != nil {
		return nil, err
	}

	err = db.Model(account).Update("balance", account.Balance+deposit).Error
	return account, err
}

func makeWithdraw(id int64, withdraw float64) (*Account, error) {
	account, err := getAccount(id)
	if err != nil {
		return nil, err
	}

	if account.Balance < withdraw {
		return nil, errors.New("Not enough balance\n")
	}

	err = db.Model(account).Update("balance", account.Balance-withdraw).Error

	return account, err
}

func makeTransfer(idSrc int64, idDes int64, transfer float64) error {
	accountSrc, err := getAccount(idSrc)
	if err != nil {
		return errors.New("Not src Account\n")
	}

	accountDes, err := getAccount(idDes)
	if err != nil {
		return errors.New("Not des Account\n")
	}

	if accountSrc.Balance < transfer {
		return errors.New("Not enough money\n")
	}

	session := db.Begin()
	if err = session.Error; err != nil {
		return err
	}

	if err = session.Model(accountSrc).Update("balance", accountSrc.Balance-transfer).Error; err != nil {
		session.Rollback()
		return err
	}

	if err = session.Model(accountDes).Update("balance", accountDes.Balance+transfer).Error; err != nil {
		session.Rollback()
		return err
	}

	return session.Commit().Error
}

func deleteAccount(id int64) error {
	account, err := getAccount(id)
	if err != nil {
		return err
	}

	return db.Delete(account).Error
}

func getAccountsNum() (int64, error) {
	var count int64
	var users []Account
	err := db.Find(&users).Count(&count).Error
	return count, err
}

func getAllAccounts() {
	// 迭代查询
	var accounts []Account
	db.Find(&accounts)
	for _, account := range accounts {
		fmt.Printf("%+v\n", account)
	}
}
