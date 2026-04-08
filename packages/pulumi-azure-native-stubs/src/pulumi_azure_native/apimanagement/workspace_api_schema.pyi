import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceApiSchemaArgs", "WorkspaceApiSchema"]

@pulumi.input_type
class WorkspaceApiSchemaArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        content_type: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        workspace_id: pulumi.Input[_builtins.str],
        components: Optional[Any] = ...,
        definitions: Optional[Any] = ...,
        schema_id: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[_builtins.str]: ...
    @content_type.setter
    def content_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Any]: ...
    @components.setter
    def components(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Optional[Any]: ...
    @definitions.setter
    def definitions(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:apimanagement:WorkspaceApiSchema")
class WorkspaceApiSchema(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        components: Optional[Any] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        definitions: Optional[Any] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceApiSchemaArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceApiSchema: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[_builtins.str]]: ...
