import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PermissionsBoundaryAttachmentArgs", "PermissionsBoundaryAttachment"]

@pulumi.input_type
class PermissionsBoundaryAttachmentArgs:
    def __init__(
        __self__,
        *,
        instance_arn: pulumi.Input[_builtins.str],
        permission_set_arn: pulumi.Input[_builtins.str],
        permissions_boundary: pulumi.Input[
            PermissionsBoundaryAttachmentPermissionsBoundaryArgs
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]: ...
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Input[_builtins.str]: ...
    @permission_set_arn.setter
    def permission_set_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryArgs]: ...
    @permissions_boundary.setter
    def permissions_boundary(
        self, value: pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PermissionsBoundaryAttachmentState:
    def __init__(
        __self__,
        *,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[
            pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission_set_arn.setter
    def permission_set_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> Optional[
        pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryArgs]
    ]: ...
    @permissions_boundary.setter
    def permissions_boundary(
        self,
        value: Optional[
            pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PermissionsBoundaryAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[
            pulumi.Input[
                Union[
                    PermissionsBoundaryAttachmentPermissionsBoundaryArgs,
                    PermissionsBoundaryAttachmentPermissionsBoundaryArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PermissionsBoundaryAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[
            pulumi.Input[
                Union[
                    PermissionsBoundaryAttachmentPermissionsBoundaryArgs,
                    PermissionsBoundaryAttachmentPermissionsBoundaryArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PermissionsBoundaryAttachment: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> pulumi.Output[outputs.PermissionsBoundaryAttachmentPermissionsBoundary]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
