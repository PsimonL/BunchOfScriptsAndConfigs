package main

import (
	"fmt"
	"sync"
	"time"
)

func multipleThreadsChannels(arr []int, wg *sync.WaitGroup, results chan int) {
	defer wg.Done()

	for i := range arr {
		arr[i]++
	}

	// For example take length, any value just to push through the channel
	results <- len(arr)
}

func driverChannels() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println("Original array:", arr)
	// sync.WaitGroup is used to synchronize multiple threads and track whether all threads have finished before the main thread continues
	var wg sync.WaitGroup
	startTime := time.Now()
	// Channel to gather goroutines outputs
	results := make(chan int)
	// Create as many threads as is cells in array
	for i := range arr {
		// Add ONE operation to wait pool, they synchronize at wg.Wait()
		wg.Add(1)
		// array slicing for each thread is each position in array
		go multipleThreadsChannels(arr[i:i+1], &wg, results)
	}
	// Wait for all threads to finish to prevent memory leaks and errors
	// All goroutines must finish by then
	go func() {
		wg.Wait()
		close(results)
	}()
	// Will produce errors, no synchronization provided
	//wg.Wait()
	// For Example sum up all outputs from goroutines
	totalProcessed := 0
	for result := range results {
		totalProcessed += result
	}
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
