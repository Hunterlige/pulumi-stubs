import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProtectionHealthCheckAssociationArgs", "ProtectionHealthCheckAssociation"]

@pulumi.input_type
class ProtectionHealthCheckAssociationArgs:
    def __init__(
        __self__,
        *,
        health_check_arn: pulumi.Input[_builtins.str],
        shield_protection_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckArn")
    def health_check_arn(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_arn.setter
    def health_check_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="shieldProtectionId")
    def shield_protection_id(self) -> pulumi.Input[_builtins.str]: ...
    @shield_protection_id.setter
    def shield_protection_id(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _ProtectionHealthCheckAssociationState:
    def __init__(
        __self__,
        *,
        health_check_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        shield_protection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckArn")
    def health_check_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_arn.setter
    def health_check_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldProtectionId")
    def shield_protection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shield_protection_id.setter
    def shield_protection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ProtectionHealthCheckAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        health_check_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        shield_protection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProtectionHealthCheckAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        health_check_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        shield_protection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ProtectionHealthCheckAssociation: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckArn")
    def health_check_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shieldProtectionId")
    def shield_protection_id(self) -> pulumi.Output[_builtins.str]: ...
