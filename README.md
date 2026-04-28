<p align="center">
  <img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" alt="seven logo" />
</p>

<h1 align="center">seven SMS for Zabbix</h1>

<p align="center">
  Notification media type for <a href="https://www.zabbix.com/">Zabbix</a> that sends SMS via the seven gateway.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-teal.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Zabbix-5.4%2B-blue" alt="Zabbix 5.4+" />
  <img src="https://img.shields.io/badge/Python-2%20|%203-yellow" alt="Python 2 | 3" />
</p>

---

## Features

- **Native Media Type** - Drop-in `seven.py` alertscript usable from any Zabbix trigger
- **Advanced Options** - Flash, TTL, performance tracking, foreign ID, label, custom sender
- **Per-User Routing** - Standard Zabbix user-media routing applies

## Prerequisites

- Zabbix (tested on 5.4) and Python 2 or 3
- A [seven account](https://www.seven.io/) with API key ([How to get your API key](https://help.seven.io/en/developer/where-do-i-find-my-api-key))

## Installation

1. Copy [`seven.py`](seven.py) into the Zabbix alertscripts directory (typically `/usr/lib/zabbix/alertscripts`).
2. Make it executable:

   ```bash
   chmod +x /usr/lib/zabbix/alertscripts/seven.py
   ```

3. Open the Zabbix web UI and navigate to **Administration > Media types**.
4. Click **Create media type** and configure as shown in [screenshots/media_type.png](screenshots/media_type.png).
5. Verify with **Test** ([screenshot](screenshots/media_type_test.png)).
6. Open **Users**, pick a user and assign the new media under **Media** ([screenshot](screenshots/user_edit.png)).

## Usage

```text
seven.py [-h] [--delay DELAY] [--flash] [--foreign_id FOREIGN_ID]
         [--from FROM] [--label LABEL] [--performance_tracking]
         [--ttl TTL] [--udh UDH]
         api_key to text
```

| Option | Description |
|--------|-------------|
| `api_key` | Your seven API key (positional) |
| `to` | Recipient phone number (positional) |
| `text` | Message body (positional) |
| `--from` | Sender ID. Up to 11 alphanumeric or 16 numeric characters |
| `--flash` | Send as flash SMS |
| `--delay` | Delayed dispatch (Unix timestamp or `yyyy-mm-dd hh:ii`) |
| `--ttl` | Time-to-live in minutes (default 2880) |
| `--foreign_id` / `--label` | Tracking metadata |
| `--performance_tracking` | Enable URL shortening and click tracking |
| `--udh` | User Data Header for binary SMS |

## Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/) or [open an issue](https://github.com/seven-io/zabbix/issues).

## License

[MIT](LICENSE)
