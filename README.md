# mlops-model-service

Мини-проект для демонстрации базового MLOps-пайплайна.

Проект обучает простую ML-модель на датасете Iris, сохраняет её в файл `model.pkl`, поднимает API-сервис на FastAPI и запускает приложение в Docker.

## Структура проекта

```text
mlops-model-service/
├── README.md
├── app/
│   ├── main.py
│   ├── model.pkl
│   └── predict.py
├── train/
│   └── train_model.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── docs/
    ├── architecture.md
    ├── troubleshooting.md
    └── api_examples.md
```

## Требования

  * fastapi       — фреймворк для API
  * uvicorn       — сервер, который запускает FastAPI-приложение
  * scikit-learn  — библиотека для обучения модели
  * joblib        — сохранение и загрузка модели
  * pydantic      — валидация входных данных в API

## Запуск локально

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train/train_model.py
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Запуск через докер

```bash
docker build -t mlops-model-service .
docker run -p 8000:8000 mlops-model-service
```

## Запуск через докер compose

```bash
docker compose up --build
```

## Проверка

```bash
curl http://127.0.0.1:8000/health

curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```