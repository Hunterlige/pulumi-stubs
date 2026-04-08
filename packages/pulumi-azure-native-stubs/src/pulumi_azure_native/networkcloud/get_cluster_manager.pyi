import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterManagerResult",
    "AwaitableGetClusterManagerResult",
    "get_cluster_manager",
    "get_cluster_manager_output",
]

@pulumi.output_type
class GetClusterManagerResult:
    def __init__(
        __self__,
        analytics_workspace_id=...,
        availability_zones=...,
        azure_api_version=...,
        cluster_versions=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        fabric_controller_id=...,
        id=...,
        identity=...,
        location=...,
        managed_resource_group_configuration=...,
        manager_extended_location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        vm_size=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterVersions")
    def cluster_versions(self) -> Sequence[outputs.ClusterAvailableVersionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fabricControllerId")
    def fabric_controller_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> Optional[outputs.ManagedResourceGroupConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managerExtendedLocation")
    def manager_extended_location(self) -> outputs.ExtendedLocationResponse: ...
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
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

class AwaitableGetClusterManagerResult(GetClusterManagerResult):
    def __await__(self): ...

def get_cluster_manager(
    cluster_manager_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterManagerResult: ...
def get_cluster_manager_output(
    cluster_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterManagerResult]: ...
