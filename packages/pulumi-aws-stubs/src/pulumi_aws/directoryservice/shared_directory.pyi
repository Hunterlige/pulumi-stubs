import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SharedDirectoryArgs", "SharedDirectory"]

@pulumi.input_type
class SharedDirectoryArgs:
    def __init__(
        __self__,
        *,
        directory_id: pulumi.Input[_builtins.str],
        target: pulumi.Input[SharedDirectoryTargetArgs],
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[_builtins.str]: ...
    @directory_id.setter
    def directory_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[SharedDirectoryTargetArgs]: ...
    @target.setter
    def target(self, value: pulumi.Input[SharedDirectoryTargetArgs]): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SharedDirectoryState:
    def __init__(
        __self__,
        *,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[SharedDirectoryTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedDirectoryId")
    def shared_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_directory_id.setter
    def shared_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[SharedDirectoryTargetArgs]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[SharedDirectoryTargetArgs]]): ...

@pulumi.type_token(...)
class SharedDirectory(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[
            pulumi.Input[
                Union[SharedDirectoryTargetArgs, SharedDirectoryTargetArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SharedDirectoryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[
            pulumi.Input[
                Union[SharedDirectoryTargetArgs, SharedDirectoryTargetArgsDict]
            ]
        ] = ...,
    ) -> SharedDirectory: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedDirectoryId")
    def shared_directory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[outputs.SharedDirectoryTarget]: ...
