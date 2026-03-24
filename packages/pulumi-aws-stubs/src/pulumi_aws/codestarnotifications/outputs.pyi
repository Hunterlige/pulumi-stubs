import builtins as _builtins
import sys
import pulumi
from typing import Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotificationRuleTarget"]

@pulumi.output_type
class NotificationRuleTarget(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
