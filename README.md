## Telegram client/bot api tools

#### Requrments:
>python 3+

Check installation
```py
# requirements modules 
pandas
telethon
configparser
telebot
```


Download repository:
```shell
git clone 
cd 
pip install -r requirements.txt
# python3 -m pip install -r requirements.txt
```
Prepare config:

```shell
cp `config.ini.example` `config.ini`
# open for edit
nano config.ini
```
--- 
### Configurate own values in `config.ini`:

#### '[App]' - section

Client parametrs for (**MTProto**) usage:
- `api_id` - api client id (example: `111111`)
- `api_hash` = api client hash (example: `1111111111111111111111111111`)

You can _**get new** one_ - [by follow the link](https://my.telegram.org/auth)
- `bot_api` - bot api token

#### '[Resend]' - section
- `receiver_id` - id of user/chat for forwarding content (example: `1212313`) 
- `watch_group` - monitoring events, user must be a member in group/channel (example: `telegram_news`)
- `watch_id` - only this IDs of user/bots in chat will lookup for new messages (example: `[-12345]`) *[default is "`Null`"]* (allow all)
- `pattern` - regexp for exclude contained messages from resending (example: `""`)

```
