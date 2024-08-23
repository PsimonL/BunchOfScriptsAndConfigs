#!/bin/bash

nmap --version

nmap -p 80 --script http-version-checker.nse <target-ip>
