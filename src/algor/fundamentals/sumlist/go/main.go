package main

import "fmt"

type Numeric interface {
	int | int8 | int16 | int32 | int64 | float32 | float64
}

func main() {
	arri := []int{1, 2, 3, 4, 5}
	arrf32 := []float32{1.0, 2.0, 3.0, 4.0, 5.0}
	arrf64 := []float32{1.0, 2.0, 3.0, 4.0, 5.0}
	sumTotalT := SumList(arri)
	sumTotalF32 := SumListFloat32(arrf32)
	sumTotalF64 := SumListFloat64(arrf64)
	fmt.Printf("sum total of type T is equal to = %v \n", sumTotalT)
	fmt.Printf("sum total of type f32 is equal to = %f \n", sumTotalF32)
	fmt.Printf("sum total of type f64 is equal to = %f \n", sumTotalF64)
}

// SumList returns the sum total of all items of type T in the slice
func SumList[T Numeric](list []T) T {
	var total T
	var index = 0
	for index < len(list) {
		total += list[index]
		index++

	}
	return total
}

// SumListInt returns the sum total of all items of type int in the slice
func SumListInt(list []int) int {
	var total int
	for _, value := range list {
		total += value
	}
	return total
}

// SumListFloat32 returns the sum total of all items of type float32 in the slice
func SumListFloat32(list []float32) float32 {
	var total float32
	for _, value := range list {
		total += value
	}
	return total
}

// SumListFloat64 returns the sum total of all items of type float64 in the slice
func SumListFloat64(list []float32) float32 {
	var total float32
	for _, value := range list {
		total += value
	}
	return total
}
