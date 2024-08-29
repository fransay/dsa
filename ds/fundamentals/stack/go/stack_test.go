package main

import "testing"

func TestStack(t *testing.T) {
	stack := Stack{container: []any{1, 2, 3, 4, 5, "one", "two", "three", "four", "five"}}

	// push
	stack.Push("un")
	stack.Push("deux")

	// pop
	stack.Pop() //

	// peek
	observedPeek := stack.Peek() //
	expectedPeek := "five"
	if observedPeek != expectedPeek {
		t.Errorf("Expected %v, Got %v", expectedPeek, observedPeek)
	}

	// IsEmpty
	observedIsEmpty := stack.IsEmpty()
	expectedIsEmpty := false
	if observedIsEmpty != expectedIsEmpty {
		t.Errorf("Expected %v, Got %v", expectedIsEmpty, observedIsEmpty)
	}

	// Size
	observedSize := stack.Size()
	expectedSize := 10
	if observedSize != expectedSize {
		t.Errorf("Expected %v Got %v", observedSize, expectedSize)
	}

}
