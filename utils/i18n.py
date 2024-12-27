from typing import Dict

from utils.singleton import Singleton


class I18n(metaclass=Singleton):
    def __init__(self):
        self.translations: Dict[str, Dict] = {
            'ru': {
                'welcome': (
                    "🎄 Добро пожаловать в Новогодний розыгрыш от Nooba Pie! 🎁\n\n"
                    "Разыгрываем 100 крутых призов! Чтобы участвовать:\n"
                    "1️⃣ Найдите секретные коды в <a href='{channels}'>каналах наших партнёров</a>\n"
                    "2️⃣ Введите их в этом боте\n"
                    "3️⃣ Получите свой приз!\n\n"
                    "Удачи в поиске! 🍀"
                ),
                'incorrect_code': (
                    "❌ Ой! Этот код неверный.\n\n"
                    "Подсказка: Правильные коды спрятаны в <a href='{channels}'>каналах партнёров</a>. "
                    "Внимательно просмотрите публикации! 🔍"
                ),
                'code_is_used': (
                    "😮 Вы нашли код от @{channel}, но кто-то оказался быстрее!\n\n"
                    "Не расстраивайтесь – впереди ещё много кодов и призов! 🎯"
                ),
                'code_is_not_used': (
                    "🎉 Поздравляем! Вы первым активировали код от @{channel}!\n\n"
                    "Ваш приз: «{prize}»\n"
                    "Чтобы получить его, напишите администратору: @{ask_for_prize}\n\n"
                    "Продолжайте искать другие коды – впереди ещё много призов! ✨"
                ),
            }
        }

    def get(self, key: str, lang: str = 'ru', **kwargs) -> str:
        # try:
        return self.translations[lang][key].format(
            **kwargs
        )


i18n = I18n()
