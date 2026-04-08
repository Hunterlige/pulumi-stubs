import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkConnectionResult",
    "AwaitableGetNetworkConnectionResult",
    "get_network_connection",
    "get_network_connection_output",
]

@pulumi.output_type
class GetNetworkConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        domain_join_type=...,
        domain_name=...,
        domain_password=...,
        domain_username=...,
        health_check_status=...,
        id=...,
        location=...,
        name=...,
        networking_resource_group_name=...,
        organization_unit=...,
        provisioning_state=...,
        subnet_id=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainPassword")
    def domain_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> _builtins.str: ...
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
    @pulumi.getter(name="networkingResourceGroupName")
    def networking_resource_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationUnit")
    def organization_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNetworkConnectionResult(GetNetworkConnectionResult):
    def __await__(self): ...

def get_network_connection(
    network_connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkConnectionResult: ...
def get_network_connection_output(
    network_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkConnectionResult]: ...
