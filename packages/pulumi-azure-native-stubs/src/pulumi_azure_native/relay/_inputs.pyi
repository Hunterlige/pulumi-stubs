import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionStateArgs",
    "ConnectionStateArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "SkuArgs",
    "SkuArgsDict",
]

class ConnectionStateArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]

@pulumi.input_type
class ConnectionStateArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ],
    ): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[
        pulumi.Input[ConnectionStateArgsDict]
    ]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[ConnectionStateArgs]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[ConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[ConnectionStateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]],
    ): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SkuTier]]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, SkuName]],
        tier: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]): ...
