import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBrokerAuthorizationResult",
    "AwaitableGetBrokerAuthorizationResult",
    "get_broker_authorization",
    "get_broker_authorization_output",
]

@pulumi.output_type
class GetBrokerAuthorizationResult:
    def __init__(
        __self__,
        authorization_policies=...,
        azure_api_version=...,
        extended_location=...,
        id=...,
        listener_ref=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(self) -> outputs.AuthorizationConfigResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="listenerRef")
    def listener_ref(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBrokerAuthorizationResult(GetBrokerAuthorizationResult):
    def __await__(self): ...

def get_broker_authorization(
    authorization_name: Optional[_builtins.str] = ...,
    broker_name: Optional[_builtins.str] = ...,
    mq_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBrokerAuthorizationResult: ...
def get_broker_authorization_output(
    authorization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    broker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mq_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBrokerAuthorizationResult]: ...
