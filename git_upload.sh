#/bin/bash
cd /zabbix-scripts/
git add .
git commit -m"$(date +%F" "%T)"
git push -u origin master
