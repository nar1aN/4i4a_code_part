# Teen Savings Bot / Бот «Карманные накопления»

---

# Русская версия

## Описание проекта

Проект посвящён адаптации раздела депозитов и накопительных счетов под подростковую аудиторию, которая только начинает формировать финансовые привычки и учиться управлять карманными деньгами.

Бот помогает:

* ставить финансовые цели;
* рассчитывать срок накопления;
* регулярно откладывать деньги;
* отслеживать прогресс;
* получать мотивацию;
* использовать систему родительских бонусов.

---

## Проблема

Большинство банковских приложений проектируются для взрослых пользователей.

Для подростков накопительные продукты часто:

* выглядят сложными;
* не вызывают интереса;
* не мотивируют копить;
* не связаны с реальными подростковыми целями.

При этом именно в подростковом возрасте:

* формируются первые финансовые привычки;
* появляется понимание ценности денег;
* рождается долгосрочная лояльность к банку.

---

## Решение

Мы предлагаем сценарий «Карманные накопления» — систему накоплений, адаптированную под подростков.

Основная идея проекта:

> превратить накопление денег из скучного банковского процесса в понятный и мотивирующий опыт.

Teen Savings Bot показывает:

* сколько времени потребуется для достижения цели;
* насколько пользователь продвинулся;
* как родители могут поддерживать финансовые привычки ребёнка.

---

## Основные функции

### Создание цели

Пользователь вводит цель и её стоимость.

Пример:

```text
Айфон 80000
```

### Расчёт срока накопления

После ввода суммы еженедельных накоплений бот рассчитывает срок достижения цели.

Пример:

```text
500
```

### Пополнение накоплений

Пополнение выполняется командой:

```text
+500
```

Бот обновляет прогресс и показывает накопленную сумму.

### Визуальный прогресс

Бот отображает процент выполнения цели и прогресс-бар:

```text
🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜
```

### Родительский режим

Команда:

```text
/parent
```

позволяет родителям поддерживать цель бонусами.

Пример:

```text
1000
```

### Система мотивации

После пополнения пользователь получает мотивирующие сообщения:

* Отличное начало;
* Ты уже близко к половине;
* Продолжай в том же духе;
* Финальный рывок.

### Достижение цели

После накопления полной суммы бот поздравляет пользователя с достижением цели и подчёркивает формирование полезной финансовой привычки.

---

## Продуктовая ценность

### Для подростков

* понятный формат накоплений;
* визуальный прогресс;
* мотивация копить регулярно;
* первые навыки финансового планирования.

### Для родителей

* участие в финансовом воспитании ребёнка;
* поддержка накопительных целей;
* инструмент совместного накопления.

### Для банка

* раннее формирование финансовых привычек;
* рост лояльности пользователей;
* увеличение вовлечённости;
* развитие семейной экосистемы банка.

---

## Целевая аудитория

### Основная аудитория

* подростки младше 18 лет;
* пользователи молодёжных банковских карт;
* школьники, получающие карманные деньги.

### Дополнительная аудитория

* родители подростков;
* семьи, заинтересованные в финансовом воспитании детей.

---

## Используемые технологии

* Python 3.11
* aiogram 3
* python-dotenv
* Telegram Bot API

---

## Структура проекта

```text
project/
│
├── bot/
│   ├── __init__.py
│   ├── bot.py
│   ├── config.py
│   ├── handlers.py
│   └── data.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
```

```bash
cd REPOSITORY_NAME
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Создание `.env`

Создайте файл `.env` в корне проекта:

```env
BOT_TOKEN=your_telegram_bot_token
```

Токен можно получить через Telegram-бота @BotFather.

### 4. Запуск проекта

```bash
python -m bot.bot
```

На Windows:

```bash
py -m bot.bot
```

---

## Сценарий демонстрации

### 1. Запуск бота

```text
/start
```

### 2. Создание цели

```text
/new
```

Пример:

```text
Айфон 80000
```

### 3. Указание суммы накоплений

```text
500
```

### 4. Пополнение

```text
+500
```

### 5. Проверка прогресса

```text
/status
```

### 6. Родительский режим

```text
/parent
```

Пример бонуса:

```text
1000
```

---

## Безопасность

Файл `.env` не должен загружаться в GitHub, так как содержит токен Telegram-бота.

Для этого используется `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
.venv/
venv/
```

---

## Возможности развития проекта

В будущем проект можно расширить:

* поддержкой нескольких целей одновременно;
* хранением данных в базе данных;
* Telegram Mini App интерфейсом;
* авторизацией родителей;
* push-напоминаниями;
* системой достижений;
* повышенной ставкой для пользователей младше 18 лет;
* интеграцией с реальными банковскими накопительными счетами.

---

# Команда проекта

Проект разработан командой «4и4а» в рамках продуктового кейса по созданию банковского приложения будущего.

Данный Telegram-бот является частью общей продуктовой концепции и демонстрирует ключевую механику сценария «Карманные накопления».

Помимо Telegram-бота, команда также работала над:

* анализом пользовательского пути (CJM);
* продуктовой стратегией;
* UX/UI-дизайном интерфейсов;
* исследованием целевой аудитории;
* концепцией адаптации накопительных продуктов для подростков;
* системой родительского участия и мотивации.

---

# English Version

## Project Description

The project adapts the idea of deposits and savings accounts for teenagers who are just starting to develop financial habits and manage pocket money.

The bot helps users:

* set financial goals;
* calculate savings timelines;
* save money regularly;
* track progress;
* receive motivation;
* use parental bonuses.

---

## Problem

Most banking applications are designed for adults.

For teenagers, savings products often:

* seem too complicated;
* look boring;
* do not motivate regular saving;
* are disconnected from real teenage goals.

At the same time, teenage years are when:

* financial habits begin to form;
* understanding of money appears;
* long-term bank loyalty is created.

---

## Solution

We propose the Pocket Savings scenario — a savings system adapted for teenagers.

Main idea:

> turn saving money from a boring banking process into a clear and motivating experience.

Teen Savings Bot shows:

* how long it will take to reach a goal;
* current progress;
* how parents can support financial habits.

---

## Key Features

### Goal Creation

The user enters a goal and its price.

Example:

```text
iPhone 80000
```

### Savings Timeline Calculation

The bot calculates how long it will take to achieve the goal based on weekly savings.

Example:

```text
500
```

### Adding Savings

The user can add money using:

```text
+500
```

The bot updates the saved amount and displays the progress.

### Visual Progress

The bot displays:

* completion percentage;
* visual progress bar.

Example:

```text
🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜
```

### Parental Mode

The command:

```text
/parent
```

allows parents to support the goal with bonuses.

Example:

```text
1000
```

### Motivation System

The bot sends motivational messages after each top-up:

* Great start;
* You are close to halfway;
* Keep going;
* Final push.

### Goal Achievement

When the goal is completed, the bot congratulates the user and highlights the creation of a healthy financial habit.

---

## Product Value

### For Teenagers

* simple savings experience;
* visual progress;
* motivation;
* first financial planning skills.

### For Parents

* participation in financial education;
* support of children’s goals;
* joint saving mechanics.

### For the Bank

* early financial habit formation;
* long-term customer loyalty;
* increased engagement;
* development of family banking ecosystems.

---

## Target Audience

### Main Audience

* teenagers under 18;
* youth banking card users;
* students receiving pocket money.

### Additional Audience

* parents of teenagers;
* families interested in financial education.

---

## Technologies

* Python 3.11
* aiogram 3
* python-dotenv
* Telegram Bot API

---

## Installation and Launch

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```env
BOT_TOKEN=your_telegram_bot_token
```

### Run the bot

```bash
python -m bot.bot
```

Windows:

```bash
py -m bot.bot
```

---

## Future Improvements

The project can be expanded with:

* multiple goals support;
* database integration;
* Telegram Mini App interface;
* parental authorization;
* push notifications;
* achievement systems;
* increased rates for users under 18;
* integration with real banking savings accounts.

---

# Team

This project was developed by the team “4и4а” as part of a product case focused on designing a future banking application.

This Telegram bot is only one part of the overall product concept and demonstrates the core mechanics of the Pocket Savings scenario.

In addition to the Telegram bot, the team also worked on:

* customer journey mapping (CJM);
* product strategy;
* UX/UI interface design;
* target audience research;
* adaptation of savings products for teenagers;
* parental participation and motivation systems.
