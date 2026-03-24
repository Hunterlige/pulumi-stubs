import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkResult",
    "AwaitableGetNetworkResult",
    "get_network",
    "get_network_output",
]

@pulumi.output_type
class GetNetworkResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone=...,
        availability_zone_id=...,
        backup_subnet_cidr=...,
        client_subnet_cidr=...,
        created_at=...,
        custom_domain_name=...,
        default_dns_prefix=...,
        display_name=...,
        id=...,
        managed_services=...,
        oci_dns_forwarding_configs=...,
        oci_network_anchor_id=...,
        oci_network_anchor_url=...,
        oci_resource_anchor_name=...,
        oci_vcn_id=...,
        oci_vcn_url=...,
        peered_cidrs=...,
        percent_progress=...,
        region=...,
        status=...,
        status_reason=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSubnetCidr")
    def client_subnet_cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultDnsPrefix")
    def default_dns_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedServices")
    def managed_services(self) -> Sequence[outputs.GetNetworkManagedServiceResult]: ...
    @_builtins.property
    @pulumi.getter(name="ociDnsForwardingConfigs")
    def oci_dns_forwarding_configs(
        self,
    ) -> Sequence[outputs.GetNetworkOciDnsForwardingConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorId")
    def oci_network_anchor_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorUrl")
    def oci_network_anchor_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociVcnId")
    def oci_vcn_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociVcnUrl")
    def oci_vcn_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peeredCidrs")
    def peered_cidrs(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetNetworkResult(GetNetworkResult):
    def __await__(self): ...

def get_network(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkResult: ...
def get_network_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkResult]: ...
