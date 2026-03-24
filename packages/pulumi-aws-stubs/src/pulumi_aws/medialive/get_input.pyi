import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetInputResult", "AwaitableGetInputResult", "get_input", "get_input_output"]

@pulumi.output_type
class GetInputResult:
    def __init__(
        __self__,
        arn=...,
        attached_channels=...,
        destinations=...,
        id=...,
        input_class=...,
        input_devices=...,
        input_partner_ids=...,
        input_source_type=...,
        media_connect_flows=...,
        name=...,
        region=...,
        role_arn=...,
        security_groups=...,
        sources=...,
        state=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="attachedChannels")
    def attached_channels(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Sequence[outputs.GetInputDestinationResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputClass")
    def input_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Sequence[outputs.GetInputInputDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="inputPartnerIds")
    def input_partner_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputSourceType")
    def input_source_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(
        self,
    ) -> Sequence[outputs.GetInputMediaConnectFlowResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetInputSourceResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetInputResult(GetInputResult):
    def __await__(self): ...

def get_input(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInputResult: ...
def get_input_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInputResult]: ...
