from datetime import timedelta
from pydantic import BaseModel, field_validator
from typing import Literal, Union


class Tariff(BaseModel):
    price: int
    description: str
    db_tariff_id: str
    subscription_period: timedelta

    @field_validator("subscription_period")
    def check_period(cls, v: timedelta):
        allowed = {
            timedelta(days=1),
            timedelta(days=3),
            timedelta(days=30),
            timedelta(days=90),
            timedelta(days=180),
            timedelta(days=360),
        }
        if v not in allowed:
            raise ValueError("invalid subscription period")
        return v


class TrialPromotionTariff(Tariff):
    price: Literal[10] = 10
    description: Literal["ShredderVPN пробный период на 3 дня"] = (
        "ShredderVPN пробный период на 3 дня"
    )
    db_tariff_id: Literal["threedays"] = "threedays"
    subscription_period: timedelta = timedelta(days=3)


class OneDayTariff(Tariff):
    price: Literal[9] = 9
    description: Literal["ShredderVPN подписка на 1 день"] = (
        "ShredderVPN подписка на 1 день"
    )
    db_tariff_id: Literal["oneday"] = "oneday"
    subscription_period: timedelta = timedelta(days=1)


class OneMonthTariff(Tariff):
    price: Literal[249] = 249
    description: Literal["ShredderVPN подписка на 1 месяц"] = (
        "ShredderVPN подписка на 1 месяц"
    )
    db_tariff_id: Literal["month"] = "month"
    subscription_period: timedelta = timedelta(days=30)


class ThreeMonthsTariff(Tariff):
    price: Literal[599] = 599
    description: Literal["ShredderVPN подписка на 3 месяца"] = (
        "ShredderVPN подписка на 3 месяца"
    )
    db_tariff_id: Literal["threemonths"] = "threemonths"
    subscription_period: timedelta = timedelta(days=90)


class SixMonthsTariff(Tariff):
    price: Literal[999] = 999
    description: Literal["ShredderVPN подписка на 6 месяцев"] = (
        "ShredderVPN подписка на 6 месяцев"
    )
    db_tariff_id: Literal["sixmonths"] = "sixmonths"
    subscription_period: timedelta = timedelta(days=180)


class OneYearTariff(Tariff):
    price: Literal[1799] = 1799
    description: Literal["ShredderVPN подписка на 1 год"] = (
        "ShredderVPN подписка на 1 год"
    )
    db_tariff_id: Literal["year"] = "year"
    subscription_period: timedelta = timedelta(days=360)


TariffUnion = Union[
    TrialPromotionTariff,
    OneDayTariff,
    OneMonthTariff,
    ThreeMonthsTariff,
    SixMonthsTariff,
    OneYearTariff,
]


def str_to_tariff(db_tariff_id: str) -> TariffUnion:
    if db_tariff_id == "year":
        return OneYearTariff()
    if db_tariff_id == "sixmonths":
        return SixMonthsTariff()
    if db_tariff_id == "threemonths":
        return ThreeMonthsTariff()
    if db_tariff_id == "month":
        return OneMonthTariff()
    if db_tariff_id == "oneday":
        return OneDayTariff()
    if db_tariff_id == "threedays":
        return TrialPromotionTariff()


def is_short_tariff(tariff: Tariff) -> bool:
    if isinstance(tariff, (TrialPromotionTariff, OneDayTariff)):
        return True
    return False


def tariff_to_human_str(tariff: Tariff) -> str | None:
    if isinstance(tariff, OneYearTariff):
        return "12 месяцев"
    if isinstance(tariff, SixMonthsTariff):
        return "6 месяцев"
    if isinstance(tariff, ThreeMonthsTariff):
        return "3 месяца"
    if isinstance(tariff, OneMonthTariff):
        return "1 месяц"
    if isinstance(tariff, OneDayTariff):
        return "1 день"
    if isinstance(tariff, TrialPromotionTariff):
        return "3 дня (пробный период)"
    return None


ALL_TARIFFS: list[Tariff] = [
    TrialPromotionTariff(),
    OneDayTariff(),
    OneMonthTariff(),
    ThreeMonthsTariff(),
    SixMonthsTariff(),
    OneYearTariff(),
]
