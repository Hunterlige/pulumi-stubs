import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetChannelResult",
    "AwaitableGetChannelResult",
    "get_channel",
    "get_channel_output",
]

@pulumi.output_type
class GetChannelResult:
    def __init__(
        __self__,
        azure_api_version=...,
        channel_type=...,
        expiration_time_if_not_activated_utc=...,
        id=...,
        message_for_activation=...,
        name=...,
        partner_topic_info=...,
        provisioning_state=...,
        readiness_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerTopicInfo")
    def partner_topic_info(self) -> Optional[outputs.PartnerTopicInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readinessState")
    def readiness_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetChannelResult(GetChannelResult):
    def __await__(self): ...

def get_channel(
    channel_name: Optional[_builtins.str] = ...,
    partner_namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetChannelResult: ...
def get_channel_output(
    channel_name: Optional[pulumi.Input[_builtins.str]] = ...,
    partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetChannelResult]: ...
