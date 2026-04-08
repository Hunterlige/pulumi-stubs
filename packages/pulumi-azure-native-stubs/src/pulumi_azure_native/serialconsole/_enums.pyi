import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["SerialPortState"]

@pulumi.type_token("azure-native:serialconsole:SerialPortState")
class SerialPortState(_builtins.str, Enum):
    ENABLED = ...
    DISABLED = ...
