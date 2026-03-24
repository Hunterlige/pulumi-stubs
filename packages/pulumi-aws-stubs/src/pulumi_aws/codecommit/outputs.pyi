import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TriggerTrigger"]

@pulumi.output_type
class TriggerTrigger(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_arn: _builtins.str,
        events: Sequence[_builtins.str],
        name: _builtins.str,
        branches: Optional[Sequence[_builtins.str]] = ...,
        custom_data: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def branches(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[_builtins.str]: ...
