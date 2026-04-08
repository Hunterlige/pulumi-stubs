import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiEntityReferenceArgs",
    "ApiEntityReferenceArgsDict",
    "CloudHsmClusterSkuArgs",
    "CloudHsmClusterSkuArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "NetworkInterfaceArgs",
    "NetworkInterfaceArgsDict",
    "NetworkProfileArgs",
    "NetworkProfileArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "SkuArgs",
    "SkuArgsDict",
]

class ApiEntityReferenceArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(
        __self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudHsmClusterSkuArgsDict(TypedDict):
    family: pulumi.Input[Union[_builtins.str, CloudHsmClusterSkuFamily]]
    name: pulumi.Input[CloudHsmClusterSkuName]
    capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CloudHsmClusterSkuArgs:
    def __init__(
        __self__,
        *,
        family: pulumi.Input[Union[_builtins.str, CloudHsmClusterSkuFamily]],
        name: pulumi.Input[CloudHsmClusterSkuName],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def family(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CloudHsmClusterSkuFamily]]: ...
    @family.setter
    def family(
        self, value: pulumi.Input[Union[_builtins.str, CloudHsmClusterSkuFamily]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[CloudHsmClusterSkuName]: ...
    @name.setter
    def name(self, value: pulumi.Input[CloudHsmClusterSkuName]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NetworkInterfaceArgsDict(TypedDict):
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(
        __self__, *, private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkProfileArgsDict(TypedDict):
    network_interfaces: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgsDict]]]
    ]
    subnet: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        network_interfaces: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]
        ] = ...,
        subnet: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): ...
