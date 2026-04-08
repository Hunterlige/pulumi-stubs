import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["PaymentChannelType"]

@pulumi.type_token("azure-native:saas:PaymentChannelType")
class PaymentChannelType(_builtins.str, Enum):
    SUBSCRIPTION_DELEGATED = ...
    CUSTOMER_DELEGATED = ...
