package _5_gin

import (
	"practice/custom/05_gin/routers"
)

func Test() {
	routers.Init()
	routers.R.Run("127.0.0.1:80")
}
