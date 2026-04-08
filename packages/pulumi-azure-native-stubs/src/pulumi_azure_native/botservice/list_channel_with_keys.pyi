import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListChannelWithKeysResult",
    "AwaitableListChannelWithKeysResult",
    "list_channel_with_keys",
    "list_channel_with_keys_output",
]

@pulumi.output_type
class ListChannelWithKeysResult:
    def __init__(
        __self__,
        changed_time=...,
        entity_tag=...,
        etag=...,
        id=...,
        kind=...,
        location=...,
        name=...,
        properties=...,
        provisioning_state=...,
        resource=...,
        setting=...,
        sku=...,
        system_data=...,
        tags=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityTag")
    def entity_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> Optional[outputs.ChannelSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Sequence[_builtins.str]: ...

class AwaitableListChannelWithKeysResult(ListChannelWithKeysResult):
    def __await__(self): ...

def list_channel_with_keys(
    channel_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListChannelWithKeysResult: ...
def list_channel_with_keys_output(
    channel_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListChannelWithKeysResult]: ...
