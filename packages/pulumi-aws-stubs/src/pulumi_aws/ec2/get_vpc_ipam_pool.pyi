import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcIpamPoolResult",
    "AwaitableGetVpcIpamPoolResult",
    "get_vpc_ipam_pool",
    "get_vpc_ipam_pool_output",
]

@pulumi.output_type
class GetVpcIpamPoolResult:
    def __init__(
        __self__,
        address_family=...,
        allocation_default_netmask_length=...,
        allocation_max_netmask_length=...,
        allocation_min_netmask_length=...,
        allocation_resource_tags=...,
        arn=...,
        auto_import=...,
        aws_service=...,
        description=...,
        filters=...,
        id=...,
        ipam_pool_id=...,
        ipam_scope_id=...,
        ipam_scope_type=...,
        locale=...,
        pool_depth=...,
        publicly_advertisable=...,
        region=...,
        source_ipam_pool_id=...,
        source_resources=...,
        state=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="allocationResourceTags")
    def allocation_resource_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoImport")
    def auto_import(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="awsService")
    def aws_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcIpamPoolFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeId")
    def ipam_scope_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeType")
    def ipam_scope_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolDepth")
    def pool_depth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAdvertisable")
    def publicly_advertisable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceResources")
    def source_resources(
        self,
    ) -> Sequence[outputs.GetVpcIpamPoolSourceResourceResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetVpcIpamPoolResult(GetVpcIpamPoolResult):
    def __await__(self): ...

def get_vpc_ipam_pool(
    allocation_resource_tags: Optional[Mapping[str, _builtins.str]] = ...,
    filters: Optional[
        Sequence[Union[GetVpcIpamPoolFilterArgs, GetVpcIpamPoolFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    ipam_pool_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcIpamPoolResult: ...
def get_vpc_ipam_pool_output(
    allocation_resource_tags: Optional[
        pulumi.Input[Optional[Mapping[str, _builtins.str]]]
    ] = ...,
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetVpcIpamPoolFilterArgs, GetVpcIpamPoolFilterArgsDict]]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    ipam_pool_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcIpamPoolResult]: ...
