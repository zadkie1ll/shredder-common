from enum import Enum
from typing import Union
from typing import Literal
from pydantic import BaseModel
from common.models.tariff import Tariff

# Типы сообщений, которыми обмениваются Monkey Island сервисы


class ConversionEvent(str, Enum):
    START = "start"
    INSTALL_VPN = "install-vpn"
    INSTALL_ON_ANDROID = "install-on-android"
    INSTALL_ON_IOS = "install-on-ios"
    INSTALL_ON_MACOS = "install-on-macos"
    INSTALL_ON_WINDOWS = "install-on-windows"
    SHOW_ABOUT = "show-about"
    SHOW_PROFILE = "show-profile"
    SHOW_QUESTIONS = "show-questions"
    SHOW_TARIFFS = "show-tariffs"
    RENEW_SUBSCRIPTION = "renew-subscription"
    HAS_TRAFFIC = "has-traffic"
    HAS_TRAFFIC_MORE_THAN_5MB = "has-traffic-more-than-5mb"
    HAS_TRAFFIC_MORE_THAN_100MB = "has-traffic-more-than-100mb"
    CREATE_INVOICE_ONE_DAY = "create-invoice-one-day"
    CREATE_INVOICE_THREE_DAYS = "create-invoice-three-days"
    CREATE_INVOICE_ONE_MONTH = "create-invoice-one-month"
    CREATE_INVOICE_THREE_MONTHS = "create-invoice-three-months"
    CREATE_INVOICE_SIX_MONTHS = "create-invoice-six-months"
    CREATE_INVOICE_ONE_YEAR = "create-invoice-one-year"
    CANCEL_AUTOPAY = "cancel-autopay"
    KEEP_AUTOPAY = "keep-autopay"
    CONFIRM_CANCEL_AUTOPAY = "confirm-cancel-autopay"


class BaseMessage(BaseModel):
    service: str
    type: str


class SendConversionMessage(BaseMessage):
    service: Literal["monkey-island-ym-stat"] = "monkey-island-ym-stat"
    type: Literal["send-conversion"] = "send-conversion"
    client_id: str
    event: ConversionEvent


class SendPurchaseMessage(BaseMessage):
    service: Literal["monkey-island-ym-stat"] = "monkey-island-ym-stat"
    type: Literal["send-purchase"] = "send-purchase"
    transaction_id: str
    client_id: str
    tariff: Tariff


# Здесь нужно поле telegram_id сделать необязательным.
# Потому что пользователи могут прийти через сайт и будет известен только email.
# Что делать в случае с мобильным приложеним пока неясно.
class NotificateUserMessage(BaseModel):
    service: Literal["monkey-island-vpn-bot"] = "monkey-island-vpn-bot"
    type: Literal["notificate-user"] = "notificate-user"
    notification_type: Literal[
        "purchase-success-autopay",
        "purchase-success-non-autopay",
        "purchase-failure-autopay",
        "purchase-failure-non-autopay",
        "subscription-expired",
        "3-days-left",
        "1-day-left",
        "nc-yesterday-created",  # пришедший вчера пользователь еще не подключился
        "referral_traffic_reached_bonus_applied",  # реферал достиг 100мб трафика
        "referral_purchase_bonus_applied",  # реферал купил подписку
    ]
    telegram_id: int


class ReferralReachedTrafficBonusApplied(NotificateUserMessage):
    service: Literal["monkey-island-vpn-bot"] = "monkey-island-vpn-bot"
    type: Literal["standard-ref-referral-traffic-reached"] = (
        "standard-ref-referral-traffic-reached"
    )
    notification_type: Literal["referral_traffic_reached_bonus_applied"] = (
        "referral_traffic_reached_bonus_applied"
    )
    telegram_id: int
    referral_reached_traffic_count: int
    bonus_days_count: int


class ReferralPurchaseBonusApplied(NotificateUserMessage):
    service: Literal["monkey-island-vpn-bot"] = "monkey-island-vpn-bot"
    type: Literal["standard-ref-referral-purchase"] = "standard-ref-referral-purchase"
    notification_type: Literal["referral_purchase_bonus_applied"] = (
        "referral_purchase_bonus_applied"
    )
    telegram_id: int
    referral_tariff: Literal[
        "oneday", "threedays", "month", "threemonths", "sixmonths", "year"
    ]
    bonus_days_count: int


MessageUnion = Union[
    SendConversionMessage,
    SendPurchaseMessage,
    NotificateUserMessage,
    ReferralReachedTrafficBonusApplied,
]
