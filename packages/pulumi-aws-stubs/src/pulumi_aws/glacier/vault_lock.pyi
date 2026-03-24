import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VaultLockArgs", "VaultLock"]

@pulumi.input_type
class VaultLockArgs:
    def __init__(
        __self__,
        *,
        complete_lock: pulumi.Input[_builtins.bool],
        policy: pulumi.Input[_builtins.str],
        vault_name: pulumi.Input[_builtins.str],
        ignore_deletion_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completeLock")
    def complete_lock(self) -> pulumi.Input[_builtins.bool]: ...
    @complete_lock.setter
    def complete_lock(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Input[_builtins.str]: ...
    @vault_name.setter
    def vault_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreDeletionError")
    def ignore_deletion_error(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_deletion_error.setter
    def ignore_deletion_error(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VaultLockState:
    def __init__(
        __self__,
        *,
        complete_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_deletion_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completeLock")
    def complete_lock(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @complete_lock.setter
    def complete_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreDeletionError")
    def ignore_deletion_error(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_deletion_error.setter
    def ignore_deletion_error(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vault_name.setter
    def vault_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:glacier/vaultLock:VaultLock")
class VaultLock(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        complete_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_deletion_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VaultLockArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        complete_lock: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_deletion_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VaultLock: ...
    @_builtins.property
    @pulumi.getter(name="completeLock")
    def complete_lock(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreDeletionError")
    def ignore_deletion_error(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Output[_builtins.str]: ...
