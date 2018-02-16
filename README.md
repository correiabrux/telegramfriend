# Telegram Friend
A little bot to get news in the telegram.

## Getting Started
Its simple, just install docker, clone repo and run. 

### Prerequisites

```
. Install Docker
. Get yout news api key - https://newsapi.org/
. Create your telegram bot https://core.telegram.org/bots/

```

### Running
```
git clone git@github.com:correiabrux/telegramfriend.git
```

```
docker run -e telegramtoken='YOURTELEGRAMKEY' -e newsapikey='YOURNEWSAPIKEY' bot
```