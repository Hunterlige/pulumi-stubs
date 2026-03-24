import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcAssociationAuthorizationArgs", "VpcAssociationAuthorization"]

@pulumi.input_type
class VpcAssociationAuthorizationArgs:
    def __init__(
        __self__,
        *,
        vpc_id: pulumi.Input[_builtins.str],
        zone_id: pulumi.Input[_builtins.str],
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @zone_id.setter
    def zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_region.setter
    def vpc_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcAssociationAuthorizationState:
    def __init__(
        __self__,
        *,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_region.setter
    def vpc_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VpcAssociationAuthorization(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcAssociationAuthorizationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcAssociationAuthorization: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
