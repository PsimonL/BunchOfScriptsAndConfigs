package main

import (
	"fmt"
	"net"
)

func Is_valid_ip(ip string) bool {
	return net.ParseIP(ip) != nil
}

func main() {
	output := Is_valid_ip("12.255.56.1")
	fmt.Println(output)
}
