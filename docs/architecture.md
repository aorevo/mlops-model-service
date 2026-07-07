# Architecture

Проект состоит из трёх основных частей:

  1. Training pipeline
  2. Model artifact
  3. API service

## 1. Training pipeline

Файл `train/train_model.py`:

  * загружает датасет Iris;
  * делит данные на train/test;
  * обучает модель `LogisticRegression`;
  * считает `accuracy`;
  * сохраняет модель в `app/model.pkl`.

## 2. Model artifact

Файл `app/model.pkl` - сериализованный объект, внутри которого лежат:

  * обученная модель;
  * названия классов;
  * названия признаков.

## 3. API service

Файлы `app/main.py` и `app/predict.py`. `main.py` отвечает за HTTP API. `predict.py` отвечает за загрузку модели и выполнение предсказания.

**flow**

```text
Client
  |
  | POST /predict
  v
FastAPI app
  |
  v
Pydantic validation
  |
  v
ModelService
  |
  v
model.pkl
  |
  v
Prediction response
```

**Docker**

Dockerfile собирает образ приложения:

  * устанавливает зависимости;
  * копирует код;
  * обучает модель;
  * запускает FastAPI через uvicorn.

**Docker Compose**

`docker-compose.yml` позволяет запускать сервис одной командой `docker compose up --build`