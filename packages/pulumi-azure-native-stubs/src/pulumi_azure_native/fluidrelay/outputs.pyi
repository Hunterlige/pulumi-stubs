import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomerManagedKeyEncryptionPropertiesResponse",
    ...,
    "EncryptionPropertiesResponse",
    "FluidRelayEndpointsResponse",
    "IdentityResponse",
    "IdentityResponseUserAssignedIdentities",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class CustomerManagedKeyEncryptionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_encryption_key_identity: Optional[
            outputs.CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity
        ] = ...,
        key_encryption_key_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(
        self,
    ) -> Optional[
        outputs.CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity
    ]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomerManagedKeyEncryptionPropertiesResponseKeyEncryptionKeyIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_type: Optional[_builtins.str] = ...,
        user_assigned_identity_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EncryptionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_managed_key_encryption: Optional[
            outputs.CustomerManagedKeyEncryptionPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(
        self,
    ) -> Optional[outputs.CustomerManagedKeyEncryptionPropertiesResponse]: ...

@pulumi.output_type
class FluidRelayEndpointsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        orderer_endpoints: Sequence[_builtins.str],
        service_endpoints: Sequence[_builtins.str],
        storage_endpoints: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ordererEndpoints")
    def orderer_endpoints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEndpoints")
    def storage_endpoints(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.IdentityResponseUserAssignedIdentities]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.IdentityResponseUserAssignedIdentities]]: ...

@pulumi.output_type
class IdentityResponseUserAssignedIdentities(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...
