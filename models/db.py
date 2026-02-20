from enum import Enum
from sqlalchemy import Enum as SQLEnum, UniqueConstraint
from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import TIMESTAMP
from sqlalchemy import ForeignKey
from sqlalchemy import Sequence
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class ReferralType(str, Enum):
    STANDARD = "STANDARD"
    ONLY_REGISTRATIONS = "ONLY_REGISTRATIONS"
    ALL_PAYMENTS_PERCENTAGE = "ALL_PAYMENTS_PERCENTAGE"


class ReferralBonusType(str, Enum):
    REGISTRATION = "REGISTRATION"
    TRAFFIC = "TRAFFIC"
    PURCHASE = "PURCHASE"


class DbMigration(Base):
    __tablename__ = "db_migrations"
    migration_id = Column(String(150), primary_key=True)


class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, Sequence("users_id_seq"), primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(256), unique=True, nullable=False)
    referred_by_id = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    referral_type = Column(
        SQLEnum(ReferralType, native_enum=False),
        nullable=True,
    )
    autopay_allow = Column(Boolean, default=True, nullable=False)
    expire_at = Column(TIMESTAMP)
    ymid = Column(BigInteger)

    __table_args__ = (Index("ix_users_username", "username"),)


class ReferralBonus(Base):
    __tablename__ = "referral_bonuses"
    id = Column(BigInteger, primary_key=True)
    referral_id = Column(BigInteger, ForeignKey("users.id"))
    referrer_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    bonus_type = Column(SQLEnum(ReferralBonusType, native_enum=False), nullable=False)
    days_added = Column(Integer)

    __table_args__ = (
        UniqueConstraint("referral_id", "bonus_type", name="uix_referral_bonus_type"),
    )


class ExpiredUsersNotification(Base):
    __tablename__ = "expired_users_notifications"
    id = Column(
        BigInteger, Sequence("expired_users_notifications_id_seq"), primary_key=True
    )
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)


class ExtendSubscriptionNotification(Base):
    __tablename__ = "extend_subscription_notifications"
    id = Column(BigInteger, Sequence("notificated_id_seq"), primary_key=True)
    three_days_before = Column(Boolean, default=False, nullable=False)
    one_day_before = Column(Boolean, default=False, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)


class NcUsersNotification(Base):
    __tablename__ = "nc_users_notifications"
    id = Column(
        BigInteger,
        Sequence("yesterday_created_not_connected_users_notifications_id_seq"),
        primary_key=True,
    )
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)


class UserTrafficProgress(Base):
    __tablename__ = "user_traffic_progress"
    id = Column(BigInteger, Sequence("user_traffic_progress_id_seq"), primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)
    passed_0 = Column(Boolean, default=False, nullable=False)
    passed_5mb = Column(Boolean, default=False, nullable=False)
    passed_100mb = Column(Boolean, default=False, nullable=False)


class YkPayment(Base):
    __tablename__ = "yk_payments"
    id = Column(BigInteger, Sequence("yk_payments_id_seq"), primary_key=True)
    is_trial_promotion = Column(Boolean, default=False, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    currency = Column(String(256), nullable=False)
    status = Column(String(256), nullable=False)
    captured_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, nullable=False)
    payment_id = Column(String(256), nullable=False)
    subscription_period = Column(String(256), nullable=False)


class YkRecurrentPayment(Base):
    __tablename__ = "yk_recurrent_payments"
    id = Column(BigInteger, Sequence("yk_recurrent_payments_id_seq"), primary_key=True)
    is_trial_promotion = Column(Boolean, default=False, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)
    currency = Column(String(256), nullable=False)
    amount = Column(Integer, nullable=False)
    recurrent_payment_id = Column(String(256), unique=True, nullable=False)
    subscription_period = Column(String(256), nullable=False)
    captured_at = Column(TIMESTAMP, nullable=False)
    scheduled_payment = Column(Boolean, default=False, nullable=False)


class EventLog(Base):
    __tablename__ = "event_logs"
    id = Column(BigInteger, Sequence("event_logs_id_seq"), primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    event_type = Column(String(256), nullable=False)
    event_payload = Column(JSONB, nullable=False, default=dict)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=func.now())

    __table_args__ = (
        Index("ix_event_logs_user_id", "user_id"),
        Index("ix_event_logs_event_type", "event_type"),
    )


class TrafficSource(Base):
    __tablename__ = "traffic_sources"
    id = Column(BigInteger, Sequence("traffic_sources_id_seq"), primary_key=True)
    name = Column(String(256), nullable=False)
    budget = Column(BigInteger, nullable=True)
