import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSignalRReplicaResult",
    "AwaitableGetSignalRReplicaResult",
    "get_signal_r_replica",
    "get_signal_r_replica_output",
]

@pulumi.output_type
class GetSignalRReplicaResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        region_endpoint_enabled=...,
        resource_stopped=...,
        sku=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
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
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceStopped")
    def resource_stopped(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ResourceSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSignalRReplicaResult(GetSignalRReplicaResult):
    def __await__(self): ...

def get_signal_r_replica(
    replica_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSignalRReplicaResult: ...
def get_signal_r_replica_output(
    replica_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSignalRReplicaResult]: ...
