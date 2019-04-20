package _2_gorm

import (
	"fmt"
	"log"
	"os"
)

const PROMPT = `Please enter number of operation:
0. Exit
1. Create new account
2. Show detail of account
3. Deposit
4. Withdraw
5. Make transfer
6. List account order by balance
7. Count Accounts
8. Delete account
9. Query all records`

func Test() {
	initDB()
	fmt.Println("Welcome bank of gorm!")

	for {
		fmt.Println(PROMPT)

		var num int
		fmt.Scanf("%d\n", &num)

		switch num {
		case 0:
			os.Exit(1)
		case 1:
			fmt.Println("Please enter <name> <balance>:")
			var name string
			var balance float64
			fmt.Scanf("%s %f\n", &name, &balance)
			if err := newAccount(name, balance); err != nil {
				log.Fatalf("%v", err)
			}
		case 2:
			fmt.Println("Please enter <id>:")
			var id int64
			fmt.Scanf("%d\n", &id)
			if account, err := getAccount(id); err != nil {
				log.Fatalf("%v", err)
			} else {
				fmt.Printf("%#v\n", account)
			}
		case 3:
			fmt.Println("Please enter <id> <deposit>:")
			var id int64
			var deposit float64
			fmt.Scanf("%d %f\n", &id, &deposit)
			if account, err := makeDeposit(id, deposit); err != nil {
				log.Fatalf("%v", err)
			} else {
				fmt.Printf("%#v\n", account)
			}
		case 4:
			fmt.Println("Please enter <id> <deposit>:")
			var id int64
			var withdraw float64
			fmt.Scanf("%d %f\n", &id, &withdraw)
			if account, err := makeWithdraw(id, withdraw); err != nil {
				log.Fatalf("%v", err)
			} else {
				fmt.Printf("%#v\n", account)
			}
		case 5:
			fmt.Println("Please enter <id src> <id des> <transfer>:")
			var idSrc int64
			var idDes int64
			var transfer float64
			fmt.Scanf("%d %d %f\n", &idSrc, &idDes, &transfer)
			if err := makeTransfer(idSrc, idDes, transfer); err != nil {
				log.Fatalf("%v", err)
			} else {
				fmt.Printf("Transfer %f from %d to %d Success!!!\n", transfer, idSrc, idDes)
			}
		case 6:
			accounts, err := getAccountsAsBalance()
			if err != nil {
				log.Fatalf("Get all accounts failed!!! %v", err)
			} else {
				for i, account := range accounts {
					fmt.Printf("%d: %#v\n", i, account)
				}
			}
		case 7:
			num, err := getAccountsNum()
			if err != nil {
				log.Fatalf("Get accounts num failed!!! %v", err)
			} else {
				fmt.Printf("Total: %d accounts\n", num)
			}
		case 8:
			fmt.Println("Please enter <id>:")
			var id int64
			fmt.Scanf("%d\n", &id)
			if err := deleteAccount(id); err != nil {
				log.Fatalf("%v", err)
			} else {
				fmt.Printf("Delete account Id: %d\n", id)
			}
		case 9:
			fmt.Println("Query all records:")
			getAllAccounts()
		}
	}

}
