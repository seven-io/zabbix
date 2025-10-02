<img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" />

# Official Plugin for [Zabbix](https://www.zabbix.com/)

## Prerequisites

- Python 2.x / 3.x
- Zabbix (tested on Zabbix 5.4)
- An API key from seven - you can create one in your [developer dashboard](https://app.seven.io/developer)

## Installation
1. Copy [seven.py](seven.py) to the Zabbix alertscripts directory - usually in ```/usr/lib/zabbix/alertscripts```
2. Make sure the script is executable by running ```chmod +x /usr/lib/zabbix/alertscripts/seven.py```
3. Open the Zabbix web interface, usually at [http://localhost/zabbix](http://localhost/zabbix)
4. Navigate to ```Administration > Media types```
5. Click "Create media type" and fill out the fields [like this](screenshots/media_type.png)
6. You can send a test SMS by clicking "Test" in the media types list and submitting a [filled in form](screenshots/media_type_test.png)
7. Go to ```Users```, choose one, go to ```Media``` and click on "Add"
8. Fill out the form [like this](./screenshots/user_edit.png)
9. Click "Add" and "Update" to save the changes


## Usage

Available options:
```
seven.py 
    [-h] 
    [--delay DELAY]
    [--flash]
    [--foreign_id FOREIGN_ID] 
    [--from FROM] 
    [--label LABEL] 
    [--performance_tracking] 
    [--ttl TTL] 
    [--udh UDH] 
    api_key to text
```


### Support
Do you need help? Feel free to [contact us](https://www.seven.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
