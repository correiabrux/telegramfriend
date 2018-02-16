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
cd telegramfriend
```

```
docker build -t bot .
```

```
docker run -e telegramtoken='YOURTELEGRAMKEY' -e newsapikey='YOURNEWSAPIKEY' bot
```

### Tests
Now, you need to send `news` on the telegram to recieve today news.


## Authors

* **Bruno Correia** - *Initial work* - [Linkedin](https://www.linkedin.com/in/bruno-leite-62825b39/)
