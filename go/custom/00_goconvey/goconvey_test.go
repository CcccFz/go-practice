package _0_goconvey

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

func TestAdd(t *testing.T) {
	Convey("将两个数相加", t, func() {
		So(Add(1, 2), ShouldEqual, 3)
	})
}

func TestSub(t *testing.T) {
	Convey("将两个数相减", t, func() {
		So(Sub(1, 2), ShouldEqual, -1)
	})
}

func TestMul(t *testing.T) {
	Convey("将两个数相乘", t, func() {
		So(Mul(3, 2), ShouldEqual, 6)
	})
}

func TestDiv(t *testing.T) {
	Convey("将两个数相除", t, func() {
		Convey("被除数为 0", func() {
			_, err := Div(10, 0)
			So(err, ShouldNotBeNil)
		})
		Convey("被除数不为 0", func() {
			num, err := Div(10, 2)
			So(err, ShouldBeNil)
			So(num, ShouldEqual, 5)
		})
	})
}
