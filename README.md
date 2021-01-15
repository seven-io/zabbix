![Sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "Sms77.io Logo")


# Official Plugin for [Zabbix](https://www.zabbix.com/)


## Installation
1. Make sure Python 2+ is installed on the system.
2. Copy [sms77.py](./sms77.py) to the Zabbix scripts directory usually in ```/usr/share/zabbix/alertscripts```.
3. Open Zabbix web interface, usually at http://localhost/zabbix
4. Go to ```Administration > Media Types```
5. Click "Create media type" and fill out the fields [like this](./screenshots/media_type.png)
6. You can send a test SMS by clicking "Test" [Fill and submit the form](./screenshots/media_type_test.png)
7. Go to ```Users```, choose one, go to ```Media``` and click on "Add"
8. Fill out the form [like this](./screenshots/user_edit.png)
9. Click "Add" and "Update" to save the changes


### Usage

Available options:
```
sms77.py 
[-h] 
[--debug]
[--delay DELAY]
[--details]
[--flash]
[--foreign_id FOREIGN_ID] 
[--from FROM] 
[--json] 
[--label LABEL] 
[--no_reload] 
[--performance_tracking] 
[--return_msg_id] 
[--ttl TTL] 
[--udh UDH] 
[--unicode]
[--utf8]
api_key to text
```


#### Support
Got stuck? Feel free to [send us an email](mailto:support@sms77.io).


