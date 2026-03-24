import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetListenerResult",
    "AwaitableGetListenerResult",
    "get_listener",
    "get_listener_output",
]

@pulumi.output_type
class GetListenerResult:
    def __init__(
        __self__,
        arn=...,
        created_at=...,
        default_actions=...,
        id=...,
        last_updated_at=...,
        listener_id=...,
        listener_identifier=...,
        name=...,
        port=...,
        protocol=...,
        region=...,
        service_arn=...,
        service_id=...,
        service_identifier=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultActions")
    def default_actions(self) -> Sequence[outputs.GetListenerDefaultActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="listenerIdentifier")
    def listener_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetListenerResult(GetListenerResult):
    def __await__(self): ...

def get_listener(
    listener_identifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    service_identifier: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetListenerResult: ...
def get_listener_output(
    listener_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetListenerResult]: ...
