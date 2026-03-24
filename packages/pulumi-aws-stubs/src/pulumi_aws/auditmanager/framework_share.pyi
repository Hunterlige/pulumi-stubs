import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FrameworkShareArgs", "FrameworkShare"]

@pulumi.input_type
class FrameworkShareArgs:
    def __init__(
        __self__,
        *,
        destination_account: pulumi.Input[_builtins.str],
        destination_region: pulumi.Input[_builtins.str],
        framework_id: pulumi.Input[_builtins.str],
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Input[_builtins.str]: ...
    @destination_account.setter
    def destination_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> pulumi.Input[_builtins.str]: ...
    @destination_region.setter
    def destination_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> pulumi.Input[_builtins.str]: ...
    @framework_id.setter
    def framework_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FrameworkShareState:
    def __init__(
        __self__,
        *,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_account: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_account.setter
    def destination_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_region.setter
    def destination_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @framework_id.setter
    def framework_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:auditmanager/frameworkShare:FrameworkShare")
class FrameworkShare(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_account: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FrameworkShareArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_account: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_region: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FrameworkShare: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
