import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcIpamPoolCidrAllocationArgs", "VpcIpamPoolCidrAllocation"]

@pulumi.input_type
class VpcIpamPoolCidrAllocationArgs:
    def __init__(
        __self__,
        *,
        ipam_pool_id: pulumi.Input[_builtins.str],
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disallowed_cidrs.setter
    def disallowed_cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcIpamPoolCidrAllocationState:
    def __init__(
        __self__,
        *,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ipam_pool_allocation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disallowed_cidrs.setter
    def disallowed_cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolAllocationId")
    def ipam_pool_allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipam_pool_allocation_id.setter
    def ipam_pool_allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_owner.setter
    def resource_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VpcIpamPoolCidrAllocation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcIpamPoolCidrAllocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed_cidrs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ipam_pool_allocation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcIpamPoolCidrAllocation: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolAllocationId")
    def ipam_pool_allocation_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
