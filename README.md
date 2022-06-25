# Installation

  - At Zabbix server
    - Install Python3
    - Copy *.py scripts to /usr/lib/zabbix/externalscripts
    - Import template *.xml into Zabbix
    - Create host "BEGET.RU___<BEGET.ru_account_login>"
    - Add macros in the host:
      - {$BEGETRU_USER} - beget.ru account login,
      - {$BEGETRU_PASS} - beget.ru account password
    - Attach template to the host
    - Discovery rule will get array of domains
    - Items and Triggers will be created
