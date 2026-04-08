import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetPoolResult", "AwaitableGetPoolResult", "get_pool", "get_pool_output"]

@pulumi.output_type
class GetPoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        dev_box_count=...,
        dev_box_definition_name=...,
        display_name=...,
        health_status=...,
        health_status_details=...,
        id=...,
        license_type=...,
        local_administrator=...,
        location=...,
        managed_virtual_network_regions=...,
        name=...,
        network_connection_name=...,
        provisioning_state=...,
        single_sign_on_status=...,
        stop_on_disconnect=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_network_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="devBoxCount")
    def dev_box_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthStatusDetails")
    def health_status_details(self) -> Sequence[outputs.HealthStatusDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAdministrator")
    def local_administrator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedVirtualNetworkRegions")
    def managed_virtual_network_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConnectionName")
    def network_connection_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnStatus")
    def single_sign_on_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stopOnDisconnect")
    def stop_on_disconnect(
        self,
    ) -> Optional[outputs.StopOnDisconnectConfigurationResponse]: ...
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
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetPoolResult(GetPoolResult):
    def __await__(self): ...

def get_pool(
    pool_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPoolResult: ...
def get_pool_output(
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPoolResult]: ...
