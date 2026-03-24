import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DedicatedIpAssignmentArgs", "DedicatedIpAssignment"]

@pulumi.input_type
class DedicatedIpAssignmentArgs:
    def __init__(
        __self__,
        *,
        destination_pool_name: pulumi.Input[_builtins.str],
        ip: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPoolName")
    def destination_pool_name(self) -> pulumi.Input[_builtins.str]: ...
    @destination_pool_name.setter
    def destination_pool_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> pulumi.Input[_builtins.str]: ...
    @ip.setter
    def ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DedicatedIpAssignmentState:
    def __init__(
        __self__,
        *,
        destination_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPoolName")
    def destination_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_pool_name.setter
    def destination_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip.setter
    def ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DedicatedIpAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DedicatedIpAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DedicatedIpAssignment: ...
    @_builtins.property
    @pulumi.getter(name="destinationPoolName")
    def destination_pool_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
