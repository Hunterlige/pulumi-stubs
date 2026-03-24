import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SigningProfilePermissionArgs", "SigningProfilePermission"]

@pulumi.input_type
class SigningProfilePermissionArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        principal: pulumi.Input[_builtins.str],
        profile_name: pulumi.Input[_builtins.str],
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_version.setter
    def profile_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_id.setter
    def statement_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_id_prefix.setter
    def statement_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SigningProfilePermissionState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_version.setter
    def profile_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_id.setter
    def statement_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_id_prefix.setter
    def statement_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class SigningProfilePermission(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SigningProfilePermissionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SigningProfilePermission: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statementIdPrefix")
    def statement_id_prefix(self) -> pulumi.Output[_builtins.str]: ...
