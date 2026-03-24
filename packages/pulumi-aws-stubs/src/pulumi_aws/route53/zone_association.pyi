import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ZoneAssociationArgs", "ZoneAssociation"]

@pulumi.input_type
class ZoneAssociationArgs:
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
class _ZoneAssociationState:
    def __init__(
        __self__,
        *,
        owning_account: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="owningAccount")
    def owning_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owning_account.setter
    def owning_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:route53/zoneAssociation:ZoneAssociation")
class ZoneAssociation(pulumi.CustomResource):
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
        args: ZoneAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        owning_account: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ZoneAssociation: ...
    @_builtins.property
    @pulumi.getter(name="owningAccount")
    def owning_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
