import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiGatewayConfigConnectionArgs", "ApiGatewayConfigConnection"]

@pulumi.input_type
class ApiGatewayConfigConnectionArgs:
    def __init__(
        __self__,
        *,
        gateway_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        config_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        source_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[_builtins.str]: ...
    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configConnectionName")
    def config_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_connection_name.setter
    def config_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hostnames(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @hostnames.setter
    def hostnames(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ApiGatewayConfigConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiGatewayConfigConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ApiGatewayConfigConnection: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostnames(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
