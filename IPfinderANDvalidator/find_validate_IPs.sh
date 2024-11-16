#!/bin/bash

file_path='./file.txt'
internal_ips=()
external_ips=()
internal_counter=0
external_counter=0

ip_pattern='\b(?:\d{1,3}\.){3}\d{1,3}\b'
while IFS= read -r line; do
    ip_matches=$(echo "$line" | grep -E -o "$ip_pattern")
    for ip in $ip_matches; do
        IFS='.' read -ra octets <<< "$ip"
        if [ "${#octets[@]}" -eq 4 ]; then
            is_valid=true
            for octet in "${octets[@]}"; do
                if [ "$octet" -lt 0 ] || [ "$octet" -gt 255 ]; then
                    is_valid=false
                    break
                fi
            done

            if [ "$is_valid" = true ]; then
                first_octet="${octets[0]}"

                if [[ "$first_octet" -eq 10 ]]; then
                    internal_counter=$((internal_counter + 1))
                    internal_ips+=("$ip")
                elif [[ "$first_octet" -eq 172 && "${octets[1]}" -ge 16 && "${octets[1]}" -le 31 ]]; then
                    internal_counter=$((internal_counter + 1))
                    internal_ips+=("$ip")
                elif [[ "$first_octet" -eq 192 && "${octets[1]}" -eq 168 ]]; then
                    internal_counter=$((internal_counter + 1))
                    internal_ips+=("$ip")
                else
                    external_counter=$((external_counter + 1))
                    external_ips+=("$ip")
                fi
            fi
        fi
    done
done < "$file_path"

echo "Before execution"
echo "Number of INTERNAL IPs = $internal_counter and list:"
printf '%s\n' "${internal_ips[@]}"
echo "Number of EXTERNAL IPs = $external_counter and list:"
printf '%s\n' "${external_ips[@]}"
echo "Listing done"
