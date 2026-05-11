import math
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from .data import users

router = Router()


def get_months(weeks):
    return round(weeks / 4.3, 1)

#START
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Teen Savings Bot\n\n"
        "Команды:\n"
        "/new — создать новую цель\n"
        "/status — посмотреть прогресс\n"
        "/parent — родительский бонус\n"
        "/reset — сбросить цель"
    )
#Command new
@router.message(Command("new"))
async def new_goal(message: Message):
    users[message.from_user.id] = {
        "step": "goal",
        "goal": None,
        "target": None,
        "weekly": None,
        "saved": 0,
    }

    await message.answer(
        "Введи цель и сумму\n\n"
        "Пример:\n"
        "Айфон 80000"
    )
#Статус достидения цели
@router.message(Command("status"))
async def status(message: Message):
    user = users.get(message.from_user.id)

    if not user or not user["target"]:
        await message.answer("Сначала создай цель через /start")
        return

    saved = user["saved"]
    target = user["target"]

    await message.answer(
        f" {user['goal']}\n"
        f" {saved}/{target}\n"
        f" {round(saved/target*100,1)}%"
    )
#Удаление цели
@router.message(Command("reset"))
async def reset(message: Message):
    users.pop(message.from_user.id, None)

    await message.answer(
        "Цель сброшена\n\n"
        "Создай новую через /new"
    )
#Добавление денег в копилку
@router.message(F.text.startswith("+"))
async def add_money(message: Message):
    user = users.get(message.from_user.id)

    if not user or not user["target"]:
        await message.answer("Сначала создай цель через /new")
        return

    try:
        amount = int(message.text.replace("+", "").strip())
    except:
        await message.answer("Формат пополнения: +500")
        return

    user["saved"] += amount

    target = user["target"]
    saved = user["saved"]

    percent = int((saved / target) * 100)
    bars = int(percent / 10)
    progress_bar = "🟩" * bars + "⬜" * (10 - bars)
    motivation = ""

    if percent < 25:
        motivation = "Отличное начало!"
    elif percent < 50:
        motivation = "Ты уже близко к половине!"
    elif percent < 75:
        motivation = "Продолжай в том же духе!"
    else:
        motivation = "Финальный рывок!"
    if saved >= target:
        await message.answer(
            f"🎉 ПОЗДРАВЛЯЕМ!\n\n"
            f"Ты накопил на: {user['goal']} 🥳\n\n"
            f"💰 Итоговая сумма: {saved}₽\n"
            f"Цель успешно достигнута!\n\n"
            f"Ты сформировал полезную финансовую привычку."
        )
        return

    await message.answer(
        f"{motivation}\n\n"
        f"Копилка пополнена на {amount}₽\n\n"
        f"Цель: {user['goal']}\n"
        f"Прогресс: {percent}%\n"
        f"{progress_bar}\n\n"
        f"Накоплено: {saved}₽ из {target}₽"
    )
#Родительский режим
@router.message(Command("parent"))
async def parent_mode(message: Message):
    user = users.get(message.from_user.id)

    if not user or not user.get("target"):
        await message.answer("Сначала создай цель через /new")
        return

    user["step"] = "parent_bonus"

    await message.answer(
        "👨‍👩‍👧 Родительский режим\n\n"
        "Родитель может поддержать цель бонусом.\n"
        "Введите сумму бонуса.\n\n"
        "Пример: 1000"
    )
#Родительский бонус
@router.message(F.text.lower().startswith("бонус"))
async def bonus(message: Message):
    user = users.get(message.from_user.id)

    try:
        amount = int(message.text.split()[1])
    except:
        await message.answer("Формат: бонус 1000")
        return

    user["saved"] += amount

    await message.answer(
        f"WOW! Родители добавили {amount}₽\n"
        f"Теперь: {user['saved']}₽"
    )

#Общий текстовый обработчик
@router.message()
async def text_handler(message: Message):
    user_id = message.from_user.id
    text = message.text

    if user_id not in users:
        users[user_id] = {"step": "goal"}

    user = users[user_id]
    if user["step"] == "parent_bonus":
        try:
            amount = int(text)
        except:
            await message.answer("Введите сумму числом. Например: 1000")
            return

        user["saved"] += amount
        user["step"] = "active"

        target = user["target"]
        saved = user["saved"]
        left = max(0, target - saved)
        percent = min(100, int((saved / target) * 100))

        bars = int(percent / 10)
        progress_bar = "🟩" * bars + "⬜" * (10 - bars)

        await message.answer(
            f"Родители поддержали цель!\n\n"
            f"🎁 Бонус: +{amount}₽\n"
            f"Цель: {user['goal']}\n\n"
            f"Прогресс: {percent}%\n"
            f"{progress_bar}\n\n"
            f"Накоплено: {saved}₽ из {target}₽\n"
            f"Осталось: {left}₽\n\n"
            f"Такой механизм помогает подростку копить регулярно, а родителям — участвовать без давления."
        )
        return
    if user["step"] == "goal":
        parts = text.split()

        try:
            target = int(parts[-1])
        except:
            await message.answer("Пример: Айфон 80000")
            return

        goal = " ".join(parts[:-1])

        user["goal"] = goal
        user["target"] = target
        user["step"] = "weekly"

        await message.answer("Сколько откладываешь в неделю?")
        return

    if user["step"] == "weekly":
        try:
            weekly = int(text)
        except:
            await message.answer("Просто число")
            return

        user["weekly"] = weekly
        user["step"] = "active"

        weeks = math.ceil(user["target"] / weekly)

        await message.answer(
            f" {weeks} недель (~{get_months(weeks)} мес.)\n\n"
            f"Пиши +500 чтобы копить"
        )
        return
#возвращение ошибки
    await message.answer("Не понял")