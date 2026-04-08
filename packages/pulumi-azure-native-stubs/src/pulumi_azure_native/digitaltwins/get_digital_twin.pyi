import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDigitalTwinResult",
    "AwaitableGetDigitalTwinResult",
    "get_digital_twin",
    "get_digital_twin_output",
]

@pulumi.output_type
class GetDigitalTwinResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_time=...,
        host_name=...,
        id=...,
        identity=...,
        last_updated_time=...,
        location=...,
        name=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.DigitalTwinsIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDigitalTwinResult(GetDigitalTwinResult):
    def __await__(self): ...

def get_digital_twin(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDigitalTwinResult: ...
def get_digital_twin_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDigitalTwinResult]: ...
