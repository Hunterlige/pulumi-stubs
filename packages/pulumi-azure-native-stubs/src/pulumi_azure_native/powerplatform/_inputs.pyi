import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnterprisePolicyIdentityArgs",
    "EnterprisePolicyIdentityArgsDict",
    "KeyPropertiesArgs",
    "KeyPropertiesArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "PropertiesEncryptionArgs",
    "PropertiesEncryptionArgsDict",
    "PropertiesLockboxArgs",
    "PropertiesLockboxArgsDict",
    "PropertiesNetworkInjectionArgs",
    "PropertiesNetworkInjectionArgsDict",
    "SubnetPropertiesArgs",
    "SubnetPropertiesArgsDict",
    "VirtualNetworkPropertiesArgs",
    "VirtualNetworkPropertiesArgsDict",
]

class EnterprisePolicyIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]

@pulumi.input_type
class EnterprisePolicyIdentityArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...

class KeyPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[KeyPropertiesArgsDict]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[KeyPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[KeyPropertiesArgs]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[KeyPropertiesArgs]]): ...

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

class PropertiesEncryptionArgsDict(TypedDict):
    key_vault: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, State]]]

@pulumi.input_type
class PropertiesEncryptionArgs:
    def __init__(
        __self__,
        *,
        key_vault: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): ...

class PropertiesLockboxArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[Union[_builtins.str, State]]]

@pulumi.input_type
class PropertiesLockboxArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): ...

class PropertiesNetworkInjectionArgsDict(TypedDict):
    virtual_networks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPropertiesArgsDict]]]
    ]

@pulumi.input_type
class PropertiesNetworkInjectionArgs:
    def __init__(
        __self__,
        *,
        virtual_networks: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPropertiesArgs]]]
    ]: ...
    @virtual_networks.setter
    def virtual_networks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPropertiesArgs]]]
        ],
    ): ...

class SubnetPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubnetPropertiesArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkPropertiesArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    subnet: NotRequired[pulumi.Input[SubnetPropertiesArgsDict]]

@pulumi.input_type
class VirtualNetworkPropertiesArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[SubnetPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetPropertiesArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetPropertiesArgs]]): ...
