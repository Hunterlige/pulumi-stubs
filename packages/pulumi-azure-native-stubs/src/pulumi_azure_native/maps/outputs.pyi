

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CorsRuleResponse', 'CorsRulesResponse', 'CreatorPropertiesResponse', 'EncryptionResponse', 'EncryptionResponseCustomerManagedKeyEncryption', 'EncryptionResponseKeyEncryptionKeyIdentity', 'LinkedResourceResponse', 'ManagedServiceIdentityResponse', 'MapsAccountPropertiesResponse', 'MapsAccountPropertiesResponseLocations', 'PrivateAtlasPropertiesResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'SkuResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse']
@pulumi.output_type
class CorsRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_origins: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CorsRulesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cors_rules: Optional[Sequence[outputs.CorsRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[Sequence[outputs.CorsRuleResponse]]:
        
        ...
    


@pulumi.output_type
class CreatorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, storage_units: _builtins.int, consumed_storage_unit_size_in_bytes: Optional[_builtins.int] = ..., total_storage_unit_size_in_bytes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUnits")
    def storage_units(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedStorageUnitSizeInBytes")
    def consumed_storage_unit_size_in_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageUnitSizeInBytes")
    def total_storage_unit_size_in_bytes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_managed_key_encryption: Optional[outputs.EncryptionResponseCustomerManagedKeyEncryption] = ..., infrastructure_encryption: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[outputs.EncryptionResponseCustomerManagedKeyEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionResponseCustomerManagedKeyEncryption(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_encryption_key_identity: Optional[outputs.EncryptionResponseKeyEncryptionKeyIdentity] = ..., key_encryption_key_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional[outputs.EncryptionResponseKeyEncryptionKeyIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionResponseKeyEncryptionKeyIdentity(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delegated_identity_client_id: Optional[_builtins.str] = ..., federated_client_id: Optional[_builtins.str] = ..., identity_type: Optional[_builtins.str] = ..., user_assigned_identity_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedIdentityClientId")
    def delegated_identity_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LinkedResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, unique_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class MapsAccountPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, unique_id: _builtins.str, cors: Optional[outputs.CorsRulesResponse] = ..., disable_local_auth: Optional[_builtins.bool] = ..., encryption: Optional[outputs.EncryptionResponse] = ..., linked_resources: Optional[Sequence[outputs.LinkedResourceResponse]] = ..., locations: Optional[Sequence[outputs.MapsAccountPropertiesResponseLocations]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.CorsRulesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedResources")
    def linked_resources(self) -> Optional[Sequence[outputs.LinkedResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[outputs.MapsAccountPropertiesResponseLocations]]:
        
        ...
    


@pulumi.output_type
class MapsAccountPropertiesResponseLocations(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateAtlasPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


