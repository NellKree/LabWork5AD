# Проект: Анализ и выявление бот-активности в социальных сетях

## Описание проекта

Этот проект реализует микросервисную архитектуру для анализа данных из социальных сетей и выявления бот-активности. Он состоит из трех взаимодействующих сервисов, упакованных в Docker-контейнеры, что позволяет легко разворачивать и масштабировать приложение.

---

## Архитектура проекта

Проект использует микросервисную архитектуру с тремя основными компонентами:
- **`data-ingestion-service`**: Отвечает за сбор данных из внешних источников (например, социальных сетей).
- **`bot-detection-service`**: Выполняет анализ данных на наличие бот-активности.
- **`data-visualization-service`**: Предоставляет визуализацию данных и результатов анализа.

Все три сервиса работают независимо, но взаимодействуют через HTTP-запросы. Они находятся в общей сети, что обеспечивает их взаимосвязь.

---

## Сервисы

### 1. `data-ingestion-service`
- **Описание**: Собирает данные из внешних источников (например, социальных сетей) и предоставляет их через HTTP-эндпоинт `/data`.
- **Порт**: `5000`
- **Основные функции**:
  - Сбор данных.
  - Передача данных в `bot-detection-service` для анализа.
- **Пример использования**:
  ```bash
  curl http://localhost:5000/data

  ### 2. `bot-detection-service`
- **Описание**: Анализирует данные на наличие бот-активности и возвращает результат (detected или clean).
- **Порт**: `5001`
- **Основные функции**:
  - Принимает данные через POST-запрос на эндпоинт /detect.
  - Возвращает результат анализа.
- **Пример использования**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"data": "test"}' http://localhost:5001/detect

  ### 3. `bot-detection-service`
- **Описание**: Предоставляет визуализацию данных, полученных из data-ingestion-service, и результатов анализа от bot-detection-service.
- **Порт**: `5002`
- **Основные функции**:
  - Получает данные из data-ingestion-service.
  - Отправляет данные в bot-detection-service для анализа.
  - Возвращает визуализацию данных и результатов анализа.
- **Пример использования**:
  ```bash
 curl http://localhost:5002/visualize```
 ## Тестирование
 Проект содержит интеграционные тесты для проверки работоспособности всех трех сервисов. Тесты написаны с использованием Python unittest.
 
 ### Запуск тестов через GitHub Actions:
Тесты автоматически выполняются при каждом пуше в ветку master или создании Pull Request'а. Результаты можно увидеть в разделе Actions на GitHub.

 ## Непрерывная интеграция и развертывание (CI/CD)
Проект использует GitHub Actions для автоматизации процесса сборки, тестирования и публикации Docker-образов.

 ### Этапы CI/CD pipeline:
- **Сборка Docker-образов**:
- Создаются образы для всех трех сервисов.
- **Запуск сервисов**:
- Образы запускаются через Docker Compose.
- **Выполнение интеграционных тестов**:
- Проверяется работоспособность каждого сервиса и их взаимодействие.
- **Публикация образов**:
- Если тесты проходят успешно, образы публикуются в Docker Hub.
