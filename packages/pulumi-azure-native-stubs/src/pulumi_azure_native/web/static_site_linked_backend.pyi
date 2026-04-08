import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StaticSiteLinkedBackendArgs", "StaticSiteLinkedBackend"]

@pulumi.input_type
class StaticSiteLinkedBackendArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        backend_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_backend_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backend_resource_id.setter
    def backend_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedBackendName")
    def linked_backend_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_backend_name.setter
    def linked_backend_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:web:StaticSiteLinkedBackend")
class StaticSiteLinkedBackend(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backend_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_backend_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StaticSiteLinkedBackendArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StaticSiteLinkedBackend: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
