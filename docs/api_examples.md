# API examples

## Healthcheck

Запрос:

```bash
curl http://127.0.0.1:8000/health
```

Ответ:

```bash
{
  "status": "ok"
}
```

## Пример предсказания

Запрос:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Ответ:

```bash
{
  "prediction": 0,
  "class_name": "setosa"
}
```