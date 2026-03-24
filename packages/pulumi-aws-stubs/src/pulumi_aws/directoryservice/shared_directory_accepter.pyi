import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SharedDirectoryAccepterArgs", "SharedDirectoryAccepter"]

@pulumi.input_type
class SharedDirectoryAccepterArgs:
    def __init__(
        __self__,
        *,
        shared_directory_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sharedDirectoryId")
    def shared_directory_id(self) -> pulumi.Input[_builtins.str]: ...
    @shared_directory_id.setter
    def shared_directory_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SharedDirectoryAccepterState:
    def __init__(
        __self__,
        *,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerDirectoryId")
    def owner_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_directory_id.setter
    def owner_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedDirectoryId")
    def shared_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_directory_id.setter
    def shared_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class SharedDirectoryAccepter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SharedDirectoryAccepterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SharedDirectoryAccepter: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerDirectoryId")
    def owner_directory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedDirectoryId")
    def shared_directory_id(self) -> pulumi.Output[_builtins.str]: ...
