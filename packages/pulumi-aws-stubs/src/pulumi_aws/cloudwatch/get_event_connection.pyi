import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventConnectionResult",
    "AwaitableGetEventConnectionResult",
    "get_event_connection",
    "get_event_connection_output",
]

@pulumi.output_type
class GetEventConnectionResult:
    def __init__(
        __self__,
        arn=...,
        authorization_type=...,
        id=...,
        kms_key_identifier=...,
        name=...,
        region=...,
        secret_arn=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...

class AwaitableGetEventConnectionResult(GetEventConnectionResult):
    def __await__(self): ...

def get_event_connection(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventConnectionResult: ...
def get_event_connection_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventConnectionResult]: ...
