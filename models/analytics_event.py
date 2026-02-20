from typing import Literal, Optional
from pydantic import BaseModel


class AnalyticsEvent(BaseModel):
    event_type: str


class SubscriptionCreated(AnalyticsEvent):
    event_type: Literal["subscription_created"] = "subscription_created"
    traffic_source: Optional[int] = None


class TrafficSourceChanged(AnalyticsEvent):
    event_type: Literal["traffic_source_changed"] = "traffic_source_changed"
    traffic_source: Optional[int] = None


class TrafficThresholdReached(AnalyticsEvent):
    event_type: Literal["traffic_threshold_reached"] = "traffic_threshold_reached"
    threshold: int


class SubscriptionExpired(AnalyticsEvent):
    event_type: Literal["subscription_expired"] = "subscription_expired"


class SubscriptionActivated(AnalyticsEvent):
    event_type: Literal["subscription_activated"] = "subscription_activated"


class ThreeDaysLeftNotified(AnalyticsEvent):
    event_type: Literal["three_days_left_notified"] = "three_days_left_notified"


class OneDayLeftNotified(AnalyticsEvent):
    event_type: Literal["one_day_left_notified"] = "one_day_left_notified"


class PaymentTrialManualSuccess(AnalyticsEvent):
    event_type: Literal["payment_trial_manual_success"] = "payment_trial_manual_success"


class PaymentTrialManualFailure(AnalyticsEvent):
    event_type: Literal["payment_trial_manual_failure"] = "payment_trial_manual_failure"


class PaymentRegularManualSuccess(AnalyticsEvent):
    event_type: Literal["payment_regular_manual_success"] = (
        "payment_regular_manual_success"
    )


class PaymentRegularManualFailure(AnalyticsEvent):
    event_type: Literal["payment_regular_manual_failure"] = (
        "payment_regular_manual_failure"
    )


class PaymentRegularAutopaySuccess(AnalyticsEvent):
    event_type: Literal["payment_regular_autopay_success"] = (
        "payment_regular_autopay_success"
    )


class PaymentRegularAutopayFailure(AnalyticsEvent):
    event_type: Literal["payment_regular_autopay_failure"] = (
        "payment_regular_autopay_failure"
    )


class PaymentTrialToRegularAutopaySuccess(AnalyticsEvent):
    event_type: Literal["payment_trial_to_regular_autopay_success"] = (
        "payment_trial_to_regular_autopay_success"
    )


class PaymentTrialToRegularAutopayFailure(AnalyticsEvent):
    event_type: Literal["payment_trial_to_regular_autopay_failure"] = (
        "payment_trial_to_regular_autopay_failure"
    )


class InstallVpnClicked(AnalyticsEvent):
    event_type: Literal["install_vpn_clicked"] = "install_vpn_clicked"


class InstallOnIosClicked(AnalyticsEvent):
    event_type: Literal["install_on_ios_clicked"] = "install_on_ios_clicked"


class InstallOnMacosClicked(AnalyticsEvent):
    event_type: Literal["install_on_macos_clicked"] = "install_on_macos_clicked"


class InstallOnWindowsClicked(AnalyticsEvent):
    event_type: Literal["install_on_windows_clicked"] = "install_on_windows_clicked"


class InstallOnAndroidClicked(AnalyticsEvent):
    event_type: Literal["install_on_android_clicked"] = "install_on_android_clicked"


class CancelAutopayClicked(AnalyticsEvent):
    event_type: Literal["cancel_autopay_clicked"] = "cancel_autopay_clicked"


class KeepAutopayClicked(AnalyticsEvent):
    event_type: Literal["keep_autopay_clicked"] = "keep_autopay_clicked"


class ConfirmCancelAutopayClicked(AnalyticsEvent):
    event_type: Literal["confirm_cancel_autopay_clicked"] = (
        "confirm_cancel_autopay_clicked"
    )


class ShowAboutClicked(AnalyticsEvent):
    event_type: Literal["show_about_clicked"] = "show_about_clicked"


class ShowProfileClicked(AnalyticsEvent):
    event_type: Literal["show_profile_clicked"] = "show_profile_clicked"


class ShowQuestionsClicked(AnalyticsEvent):
    event_type: Literal["show_questions_clicked"] = "show_questions_clicked"


class ShowTariffsClicked(AnalyticsEvent):
    event_type: Literal["show_tariffs_clicked"] = "show_tariffs_clicked"


class CreateInvoiceOneDay(AnalyticsEvent):
    event_type: Literal["create_invoice_one_day"] = "create_invoice_one_day"


class CreateInvoiceThreeDays(AnalyticsEvent):
    event_type: Literal["create_invoice_three_days"] = "create_invoice_three_days"


class CreateInvoiceOneMonth(AnalyticsEvent):
    event_type: Literal["create_invoice_one_month"] = "create_invoice_one_month"


class CreateInvoiceThreeMonths(AnalyticsEvent):
    event_type: Literal["create_invoice_three_months"] = "create_invoice_three_months"


class CreateInvoiceSixMonths(AnalyticsEvent):
    event_type: Literal["create_invoice_six_months"] = "create_invoice_six_months"


class CreateInvoiceOneYear(AnalyticsEvent):
    event_type: Literal["create_invoice_one_year"] = "create_invoice_one_year"


ANALYTICS_EVENT_CLASS_MAP = {
    "subscription_created": SubscriptionCreated,
    "traffic_source_changed": TrafficSourceChanged,
    "traffic_threshold_reached": TrafficThresholdReached,
    "subscription_expired": SubscriptionExpired,
    "subscription_activated": SubscriptionActivated,
    "three_days_left_notified": ThreeDaysLeftNotified,
    "one_day_left_notified": OneDayLeftNotified,
    "payment_trial_manual_success": PaymentTrialManualSuccess,
    "payment_trial_manual_failure": PaymentTrialManualFailure,
    "payment_regular_manual_success": PaymentRegularManualSuccess,
    "payment_regular_manual_failure": PaymentRegularManualFailure,
    "payment_regular_autopay_success": PaymentRegularAutopaySuccess,
    "payment_regular_autopay_failure": PaymentRegularAutopayFailure,
    "payment_trial_to_regular_autopay_success": PaymentTrialToRegularAutopaySuccess,
    "payment_trial_to_regular_autopay_failure": PaymentTrialToRegularAutopayFailure,
    "install_vpn_clicked": InstallVpnClicked,
    "install_on_ios_clicked": InstallOnIosClicked,
    "install_on_macos_clicked": InstallOnMacosClicked,
    "install_on_windows_clicked": InstallOnWindowsClicked,
    "install_on_android_clicked": InstallOnAndroidClicked,
    "cancel_autopay_clicked": CancelAutopayClicked,
    "keep_autopay_clicked": KeepAutopayClicked,
    "confirm_cancel_autopay_clicked": ConfirmCancelAutopayClicked,
    "show_about_clicked": ShowAboutClicked,
    "show_profile_clicked": ShowProfileClicked,
    "show_questions_clicked": ShowQuestionsClicked,
    "show_tariffs_clicked": ShowTariffsClicked,
    "create_invoice_one_day": CreateInvoiceOneDay,
    "create_invoice_three_days": CreateInvoiceThreeDays,
    "create_invoice_one_month": CreateInvoiceOneMonth,
    "create_invoice_three_months": CreateInvoiceThreeMonths,
    "create_invoice_six_months": CreateInvoiceSixMonths,
    "create_invoice_one_year": CreateInvoiceOneYear,
}
