import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
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
        automation_account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointPropertyArgs]] = ...,
        private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStatePropertyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @group_ids.setter
    def group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(
        self,
    ) -> Optional[pulumi.Input[PrivateEndpointPropertyArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(
        self, value: Optional[pulumi.Input[PrivateEndpointPropertyArgs]]
    ): ...
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
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStatePropertyArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self,
        value: Optional[pulumi.Input[PrivateLinkServiceConnectionStatePropertyArgs]],
    ): ...

@pulumi.type_token("azure-native:automation:PrivateEndpointConnection")
class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        private_endpoint: Optional[
            pulumi.Input[
                Union[PrivateEndpointPropertyArgs, PrivateEndpointPropertyArgsDict]
            ]
        ] = ...,
        private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[
                Union[
                    PrivateLinkServiceConnectionStatePropertyArgs,
                    PrivateLinkServiceConnectionStatePropertyArgsDict,
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
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(
        self,
    ) -> pulumi.Output[Optional[outputs.PrivateEndpointPropertyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> pulumi.Output[
        Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
