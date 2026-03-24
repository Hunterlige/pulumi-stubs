import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppleAppArgs", "AppleApp"]

@pulumi.input_type
class AppleAppArgs:
    def __init__(
        __self__,
        *,
        bundle_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        api_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        team_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[_builtins.str]: ...
    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_id.setter
    def api_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appStoreId")
    def app_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_store_id.setter
    def app_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AppleAppState:
    def __init__(
        __self__,
        *,
        api_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        team_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_id.setter
    def api_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appStoreId")
    def app_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_store_id.setter
    def app_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:firebase/appleApp:AppleApp")
class AppleApp(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        team_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppleAppArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        team_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AppleApp: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appStoreId")
    def app_store_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
