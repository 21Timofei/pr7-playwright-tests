# ПР7: Playwright Test

Проект с тестом счётчика на JavaScript. Проверяется исходное значение `0`, нажатие кнопки «Добавить» и результат `1`.

## Установка и запуск

Нужны Node.js 24 и npm.

```bash
git clone https://github.com/21Timofei/pr7-playwright-tests.git
cd pr7-playwright-tests
./run.sh ci
./run.sh run install:browsers
./run.sh test
```

Ожидаемый результат: **1 passed**. На компьютере с runtime Codex скрипт `run.sh` автоматически использует доступный Node.js 24. Иначе он использует Node.js из `PATH`; каталог другой установки можно задать переменной `PLAYWRIGHT_NODE_DIR`.

## Режимы работы

```bash
./run.sh run report          # HTML-отчёт последнего запуска
./run.sh run test:headed     # Запуск с окном браузера
./run.sh run test:ui         # Интерактивный режим
./run.sh run test:debug      # Пошаговая отладка
```

Сервер отчёта останавливается сочетанием `Ctrl+C`.

## Состав проекта

- `tests/counter.spec.js` — исходный тест из инструкции.
- `playwright.config.js` — Chromium, консольный и HTML-отчёты, снимок экрана и трасса при ошибке.
- `package.json` и `package-lock.json` — команды запуска и точные версии зависимостей.
- `run.sh` — запуск с браузерами и кешем npm внутри проекта.
- `scripts/verify-setup.py` — дополнительная проверка подготовки при наличии Python 3: успешный тест, учебная ошибка и восстановление правильного ожидания.
- `examples/passing-report/` — сохранённый отчёт успешного запуска.
- `examples/failure-report/` — сохранённый отчёт учебного падения со снимком экрана и трассой.
- `examples/*.txt` и `examples/verification.json` — результаты проверки.
- `README.txt` — подробная памятка и подключение собственного приложения.

Сохранённые отчёты открываются после установки npm-зависимостей:

```bash
./run.sh run report -- examples/passing-report
./run.sh run report -- examples/failure-report
```

В учебном падении последнее ожидание временно заменено на `2`, при этом браузер показывает `1`. Основной тест восстановлен и проходит. Проверены запуск с окном браузера и обычный запуск без окна.

Установки `node_modules`, браузеров, кеш npm и новые результаты тестов создаются локально. Lock-файл обеспечивает повторную установку тех же npm-зависимостей.

## Документация

- [Установка Playwright](https://playwright.dev/docs/intro)
- [Настройка Playwright Test](https://playwright.dev/docs/test-configuration)
