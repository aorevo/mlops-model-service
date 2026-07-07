# Troubleshooting

## 1. Ошибка: ModuleNotFoundError

Пример:

```bash
ModuleNotFoundError: No module named 'fastapi'
```

Причина: зависимости не установлены.

Решение:

```bash
pip install -r requirements.txt
```

## 2. Ошибка: model.pkl not found

Пример:

```bash
FileNotFoundError: app/model.pkl
```

Причина: модель ещё не была обучена или файл не лежит в нужной директории.

Решение:

```bash
python train/train_model.py
```

## 3. Порт 8000 уже занят

Пример:

```bash
Address already in use
```

Причина: на порту 8000 уже запущен другой процесс.

Решение:

```bash
sudo lsof -i :8000
```

Затем остановить процесс или запустить сервис на другом порту:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

## 4. Docker build падает на установке зависимостей

Причина: проблема с сетью, pip или зависимостями.

Решение:

```bash
docker build --no-cache -t mlops-model-service . 
```

## 5. Ошибка валидации при запросе

Пример неправильного запроса:

```bash
{
  "features": [5.1, 3.5]
}
```

Причина: модель Iris ожидает 4 признака.

Правильный запрос:

```bash
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```