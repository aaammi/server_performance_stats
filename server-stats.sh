#!/bin/bash

echo "========Server Perfomans Stats========"

echo -e "\n[CPU usage]"
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
echo "CPU usage: $cpu_usage%"

echo -e "\n[Memory Usage]"
free -h | awk '/Mem:/ {print "Total: " $2 "\nUsed: " $3 "\nFree: " $4}'
mem_percent=$(free | awk '/Mem:/ {printf("%.2f", $3/$2 * 100)}')
echo "Memory Usage Percentage: $mem_percent%"

echo -e "\n[Disk Usage]"
df -h / | awk 'NR==2 {print "Total: " $2 "\nUsed: " $3 "\nFree: " $4}'
disk_percent=$(df / | awk 'NR==2 {print $5}')
echo "Disk Usage Percentage: $disk_percent"

echo -e "\n[Top 5 Processes by CPU Usage]"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6 | awk 'NR==1 {print "PID\tCOMMAND\t\t%CPU"} NR>1 {printf "%d\t%-15s\t%.2f%%\n", $1, $2, $3}'
