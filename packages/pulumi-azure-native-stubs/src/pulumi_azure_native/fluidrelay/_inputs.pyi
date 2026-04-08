import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    "CustomerManagedKeyEncryptionPropertiesArgs",
    "CustomerManagedKeyEncryptionPropertiesArgsDict",
    "EncryptionPropertiesArgs",
    "EncryptionPropertiesArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
]

class CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgsDict(TypedDict):
    identity_type: NotRequired[pulumi.Input[CmkIdentityType]]
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgs:
    def __init__(
        __self__,
        *,
        identity_type: Optional[pulumi.Input[CmkIdentityType]] = ...,
        user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[CmkIdentityType]]: ...
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[CmkIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class CustomerManagedKeyEncryptionPropertiesArgsDict(TypedDict):
    key_encryption_key_identity: NotRequired[
        pulumi.Input[
            CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgsDict
        ]
    ]
    key_encryption_key_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomerManagedKeyEncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_encryption_key_identity: Optional[
            pulumi.Input[
                CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgs
            ]
        ] = ...,
        key_encryption_key_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(
        self,
    ) -> Optional[
        pulumi.Input[CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgs]
    ]: ...
    @key_encryption_key_identity.setter
    def key_encryption_key_identity(
        self,
        value: Optional[
            pulumi.Input[
                CustomerManagedKeyEncryptionPropertiesKeyEncryptionKeyIdentityArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionPropertiesArgsDict(TypedDict):
    customer_managed_key_encryption: NotRequired[
        pulumi.Input[CustomerManagedKeyEncryptionPropertiesArgsDict]
    ]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        customer_managed_key_encryption: Optional[
            pulumi.Input[CustomerManagedKeyEncryptionPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(
        self,
    ) -> Optional[pulumi.Input[CustomerManagedKeyEncryptionPropertiesArgs]]: ...
    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(
        self, value: Optional[pulumi.Input[CustomerManagedKeyEncryptionPropertiesArgs]]
    ): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

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
