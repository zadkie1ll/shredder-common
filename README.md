# shredder-common

Здесь хранятся общие файлы:
- pydantic модели sql для работы с БД
- тарифы (цены, интервалы действия тарифов)
- pydantic модели задач для отправки в redis

Эти файлы/скрипты нужны другим микросервисам, например:
- `shredder-vpn-bot`
- `shredder-yk-payment`
- `shredder-ym-stat`
