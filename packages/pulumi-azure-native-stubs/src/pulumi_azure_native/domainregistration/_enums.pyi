import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["DnsType"]

@pulumi.type_token("azure-native:domainregistration:DnsType")
class DnsType(_builtins.str, Enum):
    AZURE_DNS = ...
    DEFAULT_DOMAIN_REGISTRAR_DNS = ...
