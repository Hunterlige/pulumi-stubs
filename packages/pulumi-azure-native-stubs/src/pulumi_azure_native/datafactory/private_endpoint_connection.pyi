import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateEndpointConnectionArgs", "PrivateEndpointConnection"]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        factory_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[PrivateLinkConnectionApprovalRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]: ...
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkConnectionApprovalRequestArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[PrivateLinkConnectionApprovalRequestArgs]]
    ): ...

@pulumi.type_token("azure-native:datafactory:PrivateEndpointConnection")
class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    PrivateLinkConnectionApprovalRequestArgs,
                    PrivateLinkConnectionApprovalRequestArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateEndpointConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PrivateEndpointConnection: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.RemotePrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
