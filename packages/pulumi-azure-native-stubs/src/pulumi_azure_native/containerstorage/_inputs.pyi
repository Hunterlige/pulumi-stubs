import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssignmentArgs",
    "AssignmentArgsDict",
    "AzureDiskArgs",
    "AzureDiskArgsDict",
    "DiskArgs",
    "DiskArgsDict",
    "ElasticSanArgs",
    "ElasticSanArgsDict",
    "EncryptionArgs",
    "EncryptionArgsDict",
    "EphemeralDiskArgs",
    "EphemeralDiskArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "PoolTypeArgs",
    "PoolTypeArgsDict",
    "RequestsArgs",
    "RequestsArgsDict",
    "ResourcesArgs",
    "ResourcesArgsDict",
]

class AssignmentArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AssignmentArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class AzureDiskArgsDict(TypedDict):
    disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DiskArgsDict]]]]
    encryption: NotRequired[pulumi.Input[EncryptionArgsDict]]
    sku_name: NotRequired[pulumi.Input[Union[_builtins.str, AzureDiskSkuName]]]

@pulumi.input_type
class AzureDiskArgs:
    def __init__(
        __self__,
        *,
        disks: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        sku_name: Optional[pulumi.Input[Union[_builtins.str, AzureDiskSkuName]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]: ...
    @disks.setter
    def disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AzureDiskSkuName]]]: ...
    @sku_name.setter
    def sku_name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AzureDiskSkuName]]]
    ): ...

class DiskArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    reference: pulumi.Input[_builtins.str]

@pulumi.input_type
class DiskArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        reference: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def reference(self) -> pulumi.Input[_builtins.str]: ...
    @reference.setter
    def reference(self, value: pulumi.Input[_builtins.str]): ...

class ElasticSanArgsDict(TypedDict):
    encryption: NotRequired[pulumi.Input[EncryptionArgsDict]]
    sku_name: NotRequired[pulumi.Input[Union[_builtins.str, ElasticSanSkuName]]]

@pulumi.input_type
class ElasticSanArgs:
    def __init__(
        __self__,
        *,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        sku_name: Optional[pulumi.Input[Union[_builtins.str, ElasticSanSkuName]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ElasticSanSkuName]]]: ...
    @sku_name.setter
    def sku_name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticSanSkuName]]]
    ): ...

class EncryptionArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[ManagedServiceIdentityArgsDict]]

@pulumi.input_type
class EncryptionArgs:
    def __init__(
        __self__,
        *,
        key_name: pulumi.Input[_builtins.str],
        key_vault_uri: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...

class EphemeralDiskArgsDict(TypedDict):
    disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DiskArgsDict]]]]
    replicas: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class EphemeralDiskArgs:
    def __init__(
        __self__,
        *,
        disks: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]] = ...,
        replicas: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]: ...
    @disks.setter
    def disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.float]]): ...

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

class PoolTypeArgsDict(TypedDict):
    azure_disk: NotRequired[pulumi.Input[AzureDiskArgsDict]]
    elastic_san: NotRequired[pulumi.Input[ElasticSanArgsDict]]
    ephemeral_disk: NotRequired[pulumi.Input[EphemeralDiskArgsDict]]

@pulumi.input_type
class PoolTypeArgs:
    def __init__(
        __self__,
        *,
        azure_disk: Optional[pulumi.Input[AzureDiskArgs]] = ...,
        elastic_san: Optional[pulumi.Input[ElasticSanArgs]] = ...,
        ephemeral_disk: Optional[pulumi.Input[EphemeralDiskArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureDisk")
    def azure_disk(self) -> Optional[pulumi.Input[AzureDiskArgs]]: ...
    @azure_disk.setter
    def azure_disk(self, value: Optional[pulumi.Input[AzureDiskArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticSan")
    def elastic_san(self) -> Optional[pulumi.Input[ElasticSanArgs]]: ...
    @elastic_san.setter
    def elastic_san(self, value: Optional[pulumi.Input[ElasticSanArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralDisk")
    def ephemeral_disk(self) -> Optional[pulumi.Input[EphemeralDiskArgs]]: ...
    @ephemeral_disk.setter
    def ephemeral_disk(self, value: Optional[pulumi.Input[EphemeralDiskArgs]]): ...

class RequestsArgsDict(TypedDict):
    storage: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class RequestsArgs:
    def __init__(
        __self__, *, storage: Optional[pulumi.Input[_builtins.float]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ResourcesArgsDict(TypedDict):
    requests: NotRequired[pulumi.Input[RequestsArgsDict]]

@pulumi.input_type
class ResourcesArgs:
    def __init__(
        __self__, *, requests: Optional[pulumi.Input[RequestsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[RequestsArgs]]: ...
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[RequestsArgs]]): ...
