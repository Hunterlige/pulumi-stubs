import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedClusterApplicationResult",
    "AwaitableGetManagedClusterApplicationResult",
    "get_managed_cluster_application",
    "get_managed_cluster_application_output",
]

@pulumi.output_type
class GetManagedClusterApplicationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        identity=...,
        location=...,
        managed_identities=...,
        name=...,
        parameters=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        upgrade_policy=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentities")
    def managed_identities(
        self,
    ) -> Optional[Sequence[outputs.ApplicationUserAssignedIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[outputs.ApplicationUpgradePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetManagedClusterApplicationResult(GetManagedClusterApplicationResult):
    def __await__(self): ...

def get_managed_cluster_application(
    application_name: Optional[_builtins.str] = ...,
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedClusterApplicationResult: ...
def get_managed_cluster_application_output(
    application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedClusterApplicationResult]: ...
