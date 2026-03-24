import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FolderMembershipArgs", "FolderMembership"]

@pulumi.input_type
class FolderMembershipArgs:
    def __init__(
        __self__,
        *,
        folder_id: pulumi.Input[_builtins.str],
        member_id: pulumi.Input[_builtins.str],
        member_type: pulumi.Input[_builtins.str],
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Input[_builtins.str]: ...
    @folder_id.setter
    def folder_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Input[_builtins.str]: ...
    @member_id.setter
    def member_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="memberType")
    def member_type(self) -> pulumi.Input[_builtins.str]: ...
    @member_type.setter
    def member_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FolderMembershipState:
    def __init__(
        __self__,
        *,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberType")
    def member_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_type.setter
    def member_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:quicksight/folderMembership:FolderMembership")
class FolderMembership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FolderMembershipArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FolderMembership: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberType")
    def member_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
