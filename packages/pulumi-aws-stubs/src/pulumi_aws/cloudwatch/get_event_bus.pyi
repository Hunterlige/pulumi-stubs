import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventBusResult",
    "AwaitableGetEventBusResult",
    "get_event_bus",
    "get_event_bus_output",
]

@pulumi.output_type
class GetEventBusResult:
    def __init__(
        __self__,
        arn=...,
        dead_letter_configs=...,
        description=...,
        id=...,
        kms_key_identifier=...,
        log_configs=...,
        name=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfigs")
    def dead_letter_configs(
        self,
    ) -> Sequence[outputs.GetEventBusDeadLetterConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logConfigs")
    def log_configs(self) -> Sequence[outputs.GetEventBusLogConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetEventBusResult(GetEventBusResult):
    def __await__(self): ...

def get_event_bus(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventBusResult: ...
def get_event_bus_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventBusResult]: ...
