package routers

import (
	"github.com/gin-gonic/gin"

	"practice/custom/05_gin/controllers"
)

var R *gin.Engine

func Init() {
	R = gin.Default()

	R.GET("/", controllers.Index)              // http get 127.0.0.1
	R.GET("/authors/:num", controllers.Author) // http get 127.0.0.1/authors/2
	R.GET("/echo", controllers.Echo)           // http get 127.0.0.1/echo?str=hi!!!
	R.POST("/sum", controllers.Sum)            // http -f post 127.0.0.1/sum a=5 b=3
}
