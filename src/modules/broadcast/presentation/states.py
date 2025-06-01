# src/modules/broadcast/presentation/states.py

from aiogram.fsm.state import State, StatesGroup


class BroadcastStates(StatesGroup):
    text = State()
    photo = State()
    button = State()
