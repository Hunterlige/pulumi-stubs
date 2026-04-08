import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetL3NetworkResult",
    "AwaitableGetL3NetworkResult",
    "get_l3_network",
    "get_l3_network_output",
]

@pulumi.output_type
class GetL3NetworkResult:
    def __init__(
        __self__,
        associated_resource_ids=...,
        azure_api_version=...,
        cluster_id=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        extended_location=...,
        hybrid_aks_clusters_associated_ids=...,
        hybrid_aks_ipam_enabled=...,
        hybrid_aks_plugin_type=...,
        id=...,
        interface_name=...,
        ip_allocation_type=...,
        ipv4_connected_prefix=...,
        ipv6_connected_prefix=...,
        l3_isolation_domain_id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_machines_associated_ids=...,
        vlan=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse: ...
    @_builtins.property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hybridAksIpamEnabled")
    def hybrid_aks_ipam_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hybridAksPluginType")
    def hybrid_aks_plugin_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAllocationType")
    def ip_allocation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4ConnectedPrefix")
    def ipv4_connected_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6ConnectedPrefix")
    def ipv6_connected_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="l3IsolationDomainId")
    def l3_isolation_domain_id(self) -> _builtins.str: ...
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
    @_builtins.property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> _builtins.float: ...

class AwaitableGetL3NetworkResult(GetL3NetworkResult):
    def __await__(self): ...

def get_l3_network(
    l3_network_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetL3NetworkResult: ...
def get_l3_network_output(
    l3_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetL3NetworkResult]: ...
