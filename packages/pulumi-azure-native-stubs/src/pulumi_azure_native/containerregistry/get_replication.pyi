import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationResult",
    "AwaitableGetReplicationResult",
    "get_replication",
    "get_replication_output",
]

@pulumi.output_type
class GetReplicationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        region_endpoint_enabled=...,
        status=...,
        system_data=...,
        tags=...,
        type=...,
        zone_redundancy=...,
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
    def region_endpoint_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.StatusResponse: ...
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
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[_builtins.str]: ...

class AwaitableGetReplicationResult(GetReplicationResult):
    def __await__(self): ...

def get_replication(
    registry_name: Optional[_builtins.str] = ...,
    replication_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationResult: ...
def get_replication_output(
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    replication_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationResult]: ...
