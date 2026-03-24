import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserStoreArgs", "UserStore"]

@pulumi.input_type
class UserStoreArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        default_license_config: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_expired_license_auto_update: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_license_auto_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLicenseConfig")
    def default_license_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_license_config.setter
    def default_license_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableExpiredLicenseAutoUpdate")
    def enable_expired_license_auto_update(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_expired_license_auto_update.setter
    def enable_expired_license_auto_update(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLicenseAutoRegister")
    def enable_license_auto_register(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_license_auto_register.setter
    def enable_license_auto_register(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userStoreId")
    def user_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_store_id.setter
    def user_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _UserStoreState:
    def __init__(
        __self__,
        *,
        default_license_config: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_expired_license_auto_update: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_license_auto_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLicenseConfig")
    def default_license_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_license_config.setter
    def default_license_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableExpiredLicenseAutoUpdate")
    def enable_expired_license_auto_update(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_expired_license_auto_update.setter
    def enable_expired_license_auto_update(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableLicenseAutoRegister")
    def enable_license_auto_register(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_license_auto_register.setter
    def enable_license_auto_register(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userStoreId")
    def user_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_store_id.setter
    def user_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:discoveryengine/userStore:UserStore")
class UserStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_license_config: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_expired_license_auto_update: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_license_auto_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserStoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_license_config: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_expired_license_auto_update: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_license_auto_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UserStore: ...
    @_builtins.property
    @pulumi.getter(name="defaultLicenseConfig")
    def default_license_config(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableExpiredLicenseAutoUpdate")
    def enable_expired_license_auto_update(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableLicenseAutoRegister")
    def enable_license_auto_register(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userStoreId")
    def user_store_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
