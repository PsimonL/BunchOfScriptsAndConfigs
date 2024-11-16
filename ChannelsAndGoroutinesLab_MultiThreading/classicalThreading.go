package main

import (
	"fmt"
	"sync"
	"time"
)

func multipleThreads(arr []int, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := range arr {
		arr[i]++
	}
}

func singleThread(arr []int) {
	for i := range arr {
		arr[i]++
	}
}

func driverClassical() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println("Original array:", arr)
	// sync.WaitGroup is used to synchronize multiple threads and track whether all threads have finished before the main thread continues
	var wg sync.WaitGroup
	startTime := time.Now()
	// Create as many threads as is cells in array
	for i := range arr {
		// Add ONE operation to wait pool, they synchronize at wg.Wait()
		wg.Add(1)
		// array slicing for each thread is each position in array
		go multipleThreads(arr[i:i+1], &wg)
	}
	// Wait for all threads to finish to prevent memory leaks and errors
	// All goroutines must finish by then
	wg.Wait()
	// Measure time of multipleThreads()
	elapsedTime := time.Since(startTime)
	fmt.Printf("Time taken by multipleThreads: %s\n", elapsedTime)
	fmt.Println("Array after multiple threads:", arr)

	arr = []int{1, 2, 3, 4, 5}
	startTime = time.Now()
	singleThread(arr)
	// Measure time for singleThread()
	elapsedTime = time.Since(startTime)
	fmt.Printf("Time taken by singleThread: %s\n", elapsedTime)
	fmt.Println("Array after single thread:", arr)
}
