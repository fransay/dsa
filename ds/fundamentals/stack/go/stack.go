// author: francis osei annin
// date: 29/08/2024
package main

type Stack struct {
	container []any
}

// Push adds a new element on top of the stack
func (p *Stack) Push(element any) {
	p.container = append(p.container, element)
}

// Pop removes the element on top of the stack
func (p *Stack) Pop() any {
	p.container = p.container[0 : len(p.container)-1]
	return p.container[len(p.container)-1]
}

// Peek show first element on top of stack, without removing it
func (p *Stack) Peek() any {
	return p.container[len(p.container)-1]
}

// IsEmpty checks if a stack is element or not
func (p *Stack) IsEmpty() bool {
	if p.Size() != 0 {
		return false
	}
	return true
}

// Size returns the number of element in a stack
func (p *Stack) Size() any {
	return len(p.container)
}
