package controllers

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func Index(c *gin.Context) {
	c.JSON(200, gin.H{"message": "hello to Index !!!"})
}

func Author(c *gin.Context) {
	num := c.Param("num")
	if num == "1" {
		c.JSON(200, gin.H{"author": "CcccFz"})
	} else {
		c.JSON(200, gin.H{"authors": "[CcccFz, Duome]"})
	}
}

func Echo(c *gin.Context) {
	str := c.DefaultQuery("str", "null")
	c.JSON(200, gin.H{"echo": str})
}

func Sum(c *gin.Context) {
	a, _ := strconv.Atoi(c.DefaultPostForm("a", "0"))
	b, _ := strconv.Atoi(c.PostForm("b"))
	c.JSON(200, gin.H{"sum result": a + b})
}
