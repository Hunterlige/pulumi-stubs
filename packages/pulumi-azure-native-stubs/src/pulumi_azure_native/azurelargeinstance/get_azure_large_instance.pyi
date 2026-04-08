import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAzureLargeInstanceResult",
    "AwaitableGetAzureLargeInstanceResult",
    "get_azure_large_instance",
    "get_azure_large_instance_output",
]

@pulumi.output_type
class GetAzureLargeInstanceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        azure_large_instance_id=...,
        hardware_profile=...,
        hw_revision=...,
        id=...,
        location=...,
        name=...,
        network_profile=...,
        os_profile=...,
        power_state=...,
        provisioning_state=...,
        proximity_placement_group=...,
        storage_profile=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureLargeInstanceId")
    def azure_large_instance_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[outputs.HardwareProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hwRevision")
    def hw_revision(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAzureLargeInstanceResult(GetAzureLargeInstanceResult):
    def __await__(self): ...

def get_azure_large_instance(
    azure_large_instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAzureLargeInstanceResult: ...
def get_azure_large_instance_output(
    azure_large_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAzureLargeInstanceResult]: ...
