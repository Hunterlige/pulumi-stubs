import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPublicIPPrefixResult",
    "AwaitableGetPublicIPPrefixResult",
    "get_public_ip_prefix",
    "get_public_ip_prefix_output",
]

@pulumi.output_type
class GetPublicIPPrefixResult:
    def __init__(
        __self__,
        azure_api_version=...,
        custom_ip_prefix=...,
        etag=...,
        extended_location=...,
        id=...,
        ip_prefix=...,
        ip_tags=...,
        load_balancer_frontend_ip_configuration=...,
        location=...,
        name=...,
        nat_gateway=...,
        prefix_length=...,
        provisioning_state=...,
        public_ip_address_version=...,
        public_ip_addresses=...,
        resource_guid=...,
        sku=...,
        tags=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customIPPrefix")
    def custom_ip_prefix(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipPrefix")
    def ip_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[Sequence[outputs.IpTagResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerFrontendIpConfiguration")
    def load_balancer_frontend_ip_configuration(
        self,
    ) -> outputs.SubResourceResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> Optional[outputs.NatGatewayResponse]: ...
    @_builtins.property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddresses")
    def public_ip_addresses(
        self,
    ) -> Sequence[outputs.ReferencedPublicIpAddressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.PublicIPPrefixSkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetPublicIPPrefixResult(GetPublicIPPrefixResult):
    def __await__(self): ...

def get_public_ip_prefix(
    expand: Optional[_builtins.str] = ...,
    public_ip_prefix_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPublicIPPrefixResult: ...
def get_public_ip_prefix_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    public_ip_prefix_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPublicIPPrefixResult]: ...
