ПР7: подготовка Playwright Test

Результат проверки:
  Node.js 24.22.1, npm 10.9.2, Playwright Test 1.65.1.
  Chromium / Chrome Headless Shell 159.0.8154.6, сборка Playwright 1255.
  Тест прошёл с окном браузера и без окна: 1 passed.
  Учебное ожидание '2' вместо '1' дало ожидаемую ошибку.
  Снимок экрана и трасса сохранены в отдельном отчёте примера ошибки.
  Исходный тест восстановлен, последний запуск: 1 passed.

Быстрый запуск из папки ui-tests:

  ./run.sh test
  ./run.sh run report

Вторая команда открывает HTML-отчёт. Остановка сервера: Ctrl+C.
run.sh без аргументов также запускает тесты.

В проекте:
  tests/counter.spec.js - тест счётчика из инструкции: 0 -> нажатие -> 1.
  playwright.config.js - Chromium, отчёт list + HTML, снимок и trace при ошибке.
  package-lock.json - точные версии зависимостей для повторной установки.
  playwright-report/ - отчёт последнего запуска.
  .browsers/ - установленный для этого проекта браузер Chromium.
  examples/failure-report/ - сохранённый отчёт учебной ошибки с вложениями.
  examples/expected-failure.txt - вывод ошибки Expected: "2", Received: "1".
  examples/restored-pass.txt - вывод последнего успешного запуска.
  examples/verification.json - результаты проверки подготовки.

Открыть сохранённый пример ошибки:
  ./run.sh run report -- examples/failure-report

Дополнительные режимы:
  ./run.sh test -- tests/counter.spec.js
  ./run.sh run test:headed
  ./run.sh run test:ui
  ./run.sh run test:debug

Повторная установка из package-lock.json:
  ./run.sh ci
  ./run.sh run install:browsers

В архиве ui-tests.zip сохранены исходники и оба отчёта.
Для запуска распакованной копии выполните две команды повторной установки.

Окружение:
  run.sh использует доступный Node.js 24 из runtime Codex.
  На другом компьютере установите поддерживаемый Node.js с npm.
  PLAYWRIGHT_NODE_DIR позволяет указать каталог с нужным исполняемым node.
  Браузеры и кеш npm хранятся в .browsers/ и .npm-cache/ внутри проекта.

Следующий этап - тест своего приложения (раздел 4 инструкции):
  1. Запустить приложение и определить его URL и проверяемый сценарий.
  2. Создать tests/application.spec.js с page.goto('URL приложения').
  3. Для записи действий запустить:
       ./run.sh exec -- playwright codegen http://localhost:3000
     Подставить адрес своего приложения вместо примера.
  4. Добавить проверку ожидаемого результата и запустить:
       ./run.sh test -- tests/application.spec.js

В текущей задаче адрес и исходники своего приложения не предоставлены.
Подготовка выполняется на автономном примере счётчика из PDF.

Официальная документация:
  https://playwright.dev/docs/intro
  https://playwright.dev/docs/test-configuration
