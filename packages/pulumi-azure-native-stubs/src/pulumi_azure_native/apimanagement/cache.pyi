import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CacheArgs", "Cache"]

@pulumi.input_type
class CacheArgs:
    def __init__(
        __self__,
        *,
        connection_string: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        use_from_location: pulumi.Input[_builtins.str],
        cache_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[_builtins.str]: ...
    @connection_string.setter
    def connection_string(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useFromLocation")
    def use_from_location(self) -> pulumi.Input[_builtins.str]: ...
    @use_from_location.setter
    def use_from_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cacheId")
    def cache_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_id.setter
    def cache_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:apimanagement:Cache")
class Cache(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_string: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_from_location: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CacheArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Cache: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useFromLocation")
    def use_from_location(self) -> pulumi.Output[_builtins.str]: ...
