# Шаблон для старта проекта по автоматизации тестирования
#### За основу взят корпоративный фреймворк [AQAS](http://git.int.kronshtadt.ru/kt_asu_gis/qa/framework/web_python)

## Старт нового проекта
1. **Копирование**
    1. Скопировать содержимое данного проекта в репозиторий с новым проектом по автоматизации
    2. Собрать проект локально, запустить имеющиеся автотесты. Убедиться в их работе, сгенерировать Allure-отчет. [Вспомогательные команды](https://confluence.steor.tech/pages/viewpage.action?pageId=47435527#id-Общиерекомендацииприиспользованиифреймворканапроектахавтоматизациитестирования-Вспомогательныекоманды)
2. **Адаптация**
    1. Удалить \ изменить скопированные подмодули и их содержимое(файлы), добавить недостающие для старта проекта(придерживаясь общей структуры). Обновить по необходимости `.gitignore`
    2. Обновить `config.json` с настройками под новый проект
    3. Убрать лишние \ добавить недостающие зависимости в `requirements.txt`
    4. При необходимости, обновить `.flake8, pyproject.toml`. Изменения в Coding style guidelines для текущего проекта **обязательно** описать в `README.md`
    5. Создать страницу на Confluence в соответствующем проекте с описанием автоматизации: адреса AQA окружения(инфраструктура), используемые учетные данные, состав команды, ссылка на проект в GitLab и Jenkins, ссылка на борд с задачами автоматизации и др. Ссылку приеркпить в `README.md`.
    6. Обновить `README.md` с описанием нового проекта(структура проекта, жизненный цикл кода в проекте и Coding style guidelines(в случае изменений) - либо ссылаться на фреймворк, команды для сборки и запуска, правила и другая важная информация). Указать ссылки на Фреймворк, Confluence, Jenkins и другие важные источники. **Не забывать дорабатывать его при реализации автотестов.**
3. **Конфигурация**
    1. Обновить при необходимости `.gitlab-ci.yml`. Описать новые pipeline в `README.md`.
    2. Создать новый проект в Jenkins, настроить job'ы для запусков автотестов(согласно требованиям проекта)

## Общая структура проекта
- `utils` - Модуль вспомогательных утилит в рамках текущего проекта
    - `json_utils.py` - Файл с вспомогательными методами по работе с Json
    - `<...>` 
- `tests` - Модуль с реализованными автотестами
    - `conftest.py` - Файл с фикстурами для всех автотестов
    - `ui` - Автотесты по взаимодействию с ui-частью
        - `test_example.py` - Файл с автотестами
        - `conftest.py` - Файл с фикстурами для автотестов ui-части
        - `sub_module` - Подмодуль с автотестами ui-части
            - `<...>`
    - `api` - Автотесты по взаимодействию с API(GraphQL)
        - `<...>`
    - `db` - Автотесты по взаимодействию с БД(PostgresQL)
        - `<...>`
    - `<...>` - Другие подмодули с автотестами
- `steps` - Модуль с реализацией общих шагов для автотестов
    - `ui`
        - `authorization_steps.py`
        - `<...>`
    - `<...>`
- `models` - Модуль с реализацией классов\моделей для автотестов
    - `ui`
        - `forms`
            - `main_page_form.py`
            - `<...>`
    - `api`
        - `adapter`
            - `geodata_adapter.py`
            - `<...>`
    - `<...>`
- `resources` - Модуль с доп.файлами для реализации автотестов: 
    - `.img, .txt, .json и др.`
    - `<...>`
- `constants.py` - Файт с константами для использования во всем проекте. Можно помещать аналогичные файлы в конкретные модули, если константы относятся только к нему. **Логины, пароли и другие конфиденциальные данные хранить в константах ЗАПРЕЩЕНО!**
- `.flake8, pyproject.toml` - Файлы для проверки соблюдения [Coding style guidelines](https://confluence.steor.tech/pages/viewpage.action?pageId=47435527#id-Общиерекомендацииприиспользованиифреймворканапроектахавтоматизациитестирования-Codingstyleguidelines)
- `.gitignore` - Файл для Git, с правилами индексации файлов для попадания в репозиторий
- `.gitlab-ci.yml` - Файл для GitLab CI\CD. необходим для автоматичесой проверки кода на [Coding style guidelines](https://confluence.steor.tech/pages/viewpage.action?pageId=47435527#id-Общиерекомендацииприиспользованиифреймворканапроектахавтоматизациитестирования-Codingstyleguidelines) или других действий. Настраивается по требованиям для конкретного проекта.
- `README.md` - Файл с описанием текущего проекта.
- `requirements.txt` - Файл со списком всех необходимых зависимостей для сборки текущего проекта и запуска автотестов.
- `config.json` - Файл с конфигурацией для модулей фреймворка в рамках текущего проекта.
- И другие модули \ файлы при необходимости.
