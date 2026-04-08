import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagementLockByScopeArgs", "ManagementLockByScope"]

@pulumi.input_type
class ManagementLockByScopeArgs:
    def __init__(
        __self__,
        *,
        level: pulumi.Input[Union[_builtins.str, LockLevel]],
        scope: pulumi.Input[_builtins.str],
        lock_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Input[Union[_builtins.str, LockLevel]]: ...
    @level.setter
    def level(self, value: pulumi.Input[Union[_builtins.str, LockLevel]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lockName")
    def lock_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lock_name.setter
    def lock_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]]: ...
    @owners.setter
    def owners(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]],
    ): ...

@pulumi.type_token("azure-native:authorization:ManagementLockByScope")
class ManagementLockByScope(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        level: Optional[pulumi.Input[Union[_builtins.str, LockLevel]]] = ...,
        lock_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owners: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ManagementLockOwnerArgs, ManagementLockOwnerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagementLockByScopeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagementLockByScope: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def owners(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ManagementLockOwnerResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
