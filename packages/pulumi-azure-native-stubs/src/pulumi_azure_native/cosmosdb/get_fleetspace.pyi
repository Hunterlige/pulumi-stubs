import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFleetspaceResult",
    "AwaitableGetFleetspaceResult",
    "get_fleetspace",
    "get_fleetspace_output",
]

@pulumi.output_type
class GetFleetspaceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_regions=...,
        fleetspace_api_kind=...,
        id=...,
        name=...,
        provisioning_state=...,
        service_tier=...,
        system_data=...,
        throughput_pool_configuration=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataRegions")
    def data_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fleetspaceApiKind")
    def fleetspace_api_kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceTier")
    def service_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="throughputPoolConfiguration")
    def throughput_pool_configuration(
        self,
    ) -> Optional[outputs.FleetspacePropertiesResponseThroughputPoolConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFleetspaceResult(GetFleetspaceResult):
    def __await__(self): ...

def get_fleetspace(
    fleet_name: Optional[_builtins.str] = ...,
    fleetspace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFleetspaceResult: ...
def get_fleetspace_output(
    fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFleetspaceResult]: ...
