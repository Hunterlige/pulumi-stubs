import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcEndpointServiceResult",
    "AwaitableGetVpcEndpointServiceResult",
    "get_vpc_endpoint_service",
    "get_vpc_endpoint_service_output",
]

@pulumi.output_type
class GetVpcEndpointServiceResult:
    def __init__(
        __self__,
        acceptance_required=...,
        arn=...,
        availability_zones=...,
        base_endpoint_dns_names=...,
        filters=...,
        id=...,
        manages_vpc_endpoints=...,
        owner=...,
        private_dns_name=...,
        private_dns_names=...,
        region=...,
        service=...,
        service_id=...,
        service_name=...,
        service_region=...,
        service_regions=...,
        service_type=...,
        supported_ip_address_types=...,
        tags=...,
        vpc_endpoint_policy_supported=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptanceRequired")
    def acceptance_required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseEndpointDnsNames")
    def base_endpoint_dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetVpcEndpointServiceFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managesVpcEndpoints")
    def manages_vpc_endpoints(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsNames")
    def private_dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use service_region instead.""")
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRegion")
    def service_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRegions")
    def service_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedIpAddressTypes")
    def supported_ip_address_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointPolicySupported")
    def vpc_endpoint_policy_supported(self) -> _builtins.bool: ...

class AwaitableGetVpcEndpointServiceResult(GetVpcEndpointServiceResult):
    def __await__(self): ...

def get_vpc_endpoint_service(
    filters: Optional[
        Sequence[
            Union[GetVpcEndpointServiceFilterArgs, GetVpcEndpointServiceFilterArgsDict]
        ]
    ] = ...,
    service: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    service_regions: Optional[Sequence[_builtins.str]] = ...,
    service_type: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcEndpointServiceResult: ...
def get_vpc_endpoint_service_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetVpcEndpointServiceFilterArgs,
                        GetVpcEndpointServiceFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    service: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    service_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcEndpointServiceResult]: ...
