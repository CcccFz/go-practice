package _6_linkedlist

import (
	"testing"

	"github.com/stretchr/testify/suite"
)

type SingleLinkedListAlgoTestSuite struct {
	suite.Suite
	l *LinkedList
}

func TestGenTestSuite(t *testing.T) {
	suite.Run(t, new(SingleLinkedListAlgoTestSuite))
}

func (s *SingleLinkedListAlgoTestSuite) SetupTest() {
	s.l = NewLinkedList()

	for i := 0; i < 5; i++ {
		s.l.InsertToTail(i+1)
	}
}

func (s *SingleLinkedListAlgoTestSuite) TestReverse() {
	s.l.Reverse()
	s.Equal(uint(5), s.l.Len())
	s.Equal("5, 4, 3, 2, 1", s.l.String())
}

func (s *SingleLinkedListAlgoTestSuite) TestMerge() {
	l1, l2 := NewLinkedList(), NewLinkedList()

	for i := 1; i <= 5; i++ {
		l1.InsertToTail(2 * i - 1)
	}

	for i := 1; i <= 5; i++ {
		l2.InsertToTail(2 * i)
	}

	s.Equal("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", Merge(l1, l2).String())
}

func (s *SingleLinkedListAlgoTestSuite) TestDeleteBottomN() {
	s.l.DeleteBottomN(0)
	s.Equal("1, 2, 3, 4, 5", s.l.String())

	s.l.DeleteBottomN(1)
	s.Equal("1, 2, 3, 4", s.l.String())

	s.l.DeleteBottomN(2)
	s.Equal("1, 2, 4", s.l.String())

	s.l.DeleteBottomN(3)
	s.Equal("2, 4", s.l.String())

	s.l.DeleteBottomN(2)
	s.Equal("4", s.l.String())

	s.l.DeleteBottomN(3)
	s.Equal("4", s.l.String())
}

func (s *SingleLinkedListAlgoTestSuite) TestHasCircle() {
	s.Equal(false, s.l.HasCircle())

	cur := s.l.head
	for cur.next != nil {
		cur = cur.next
	}
	cur.next = s.l.head.next.next

	s.Equal(true, s.l.HasCircle())
}

func (s *SingleLinkedListAlgoTestSuite) TestFindMiddleNode() {
	s.Equal(3, s.l.FindMiddleNode().val)
}