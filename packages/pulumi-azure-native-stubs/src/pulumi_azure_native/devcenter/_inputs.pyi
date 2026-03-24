

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'CustomerManagedKeyEncryptionArgs', 'CustomerManagedKeyEncryptionArgsDict', 'DevCenterProjectCatalogSettingsArgs', 'DevCenterProjectCatalogSettingsArgsDict', 'EncryptionArgs', 'EncryptionArgsDict', 'GitCatalogArgs', 'GitCatalogArgsDict', 'ImageReferenceArgs', 'ImageReferenceArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'ProjectCatalogSettingsArgs', 'ProjectCatalogSettingsArgsDict', ..., ..., 'ResourcePolicyArgs', 'ResourcePolicyArgsDict', 'SkuArgs', 'SkuArgsDict', 'StopOnDisconnectConfigurationArgs', 'StopOnDisconnectConfigurationArgsDict', 'UserRoleAssignmentArgs', 'UserRoleAssignmentArgsDict']
class CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgsDict(TypedDict):
    
    delegated_identity_client_id: NotRequired[pulumi.Input[_builtins.str]]
    identity_type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs:
    def __init__(__self__, *, delegated_identity_client_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ..., user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedIdentityClientId")
    def delegated_identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_identity_client_id.setter
    def delegated_identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomerManagedKeyEncryptionArgsDict(TypedDict):
    
    key_encryption_key_identity: NotRequired[pulumi.Input[CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgsDict]]
    key_encryption_key_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedKeyEncryptionArgs:
    def __init__(__self__, *, key_encryption_key_identity: Optional[pulumi.Input[CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs]] = ..., key_encryption_key_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional[pulumi.Input[CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs]]:
        
        ...
    
    @key_encryption_key_identity.setter
    def key_encryption_key_identity(self, value: Optional[pulumi.Input[CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DevCenterProjectCatalogSettingsArgsDict(TypedDict):
    
    catalog_item_sync_enable_status: NotRequired[pulumi.Input[Union[_builtins.str, CatalogItemSyncEnableStatus]]]


@pulumi.input_type
class DevCenterProjectCatalogSettingsArgs:
    def __init__(__self__, *, catalog_item_sync_enable_status: Optional[pulumi.Input[Union[_builtins.str, CatalogItemSyncEnableStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogItemSyncEnableStatus")
    def catalog_item_sync_enable_status(self) -> Optional[pulumi.Input[Union[_builtins.str, CatalogItemSyncEnableStatus]]]:
        
        ...
    
    @catalog_item_sync_enable_status.setter
    def catalog_item_sync_enable_status(self, value: Optional[pulumi.Input[Union[_builtins.str, CatalogItemSyncEnableStatus]]]): # -> None:
        ...
    


class EncryptionArgsDict(TypedDict):
    customer_managed_key_encryption: NotRequired[pulumi.Input[CustomerManagedKeyEncryptionArgsDict]]


@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *, customer_managed_key_encryption: Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]]:
        
        ...
    
    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(self, value: Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]]): # -> None:
        ...
    


class GitCatalogArgsDict(TypedDict):
    
    branch: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    secret_identifier: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GitCatalogArgs:
    def __init__(__self__, *, branch: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., secret_identifier: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_identifier.setter
    def secret_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ImageReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImageReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ProjectCatalogSettingsArgsDict(TypedDict):
    
    catalog_item_sync_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CatalogItemType]]]]]


@pulumi.input_type
class ProjectCatalogSettingsArgs:
    def __init__(__self__, *, catalog_item_sync_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CatalogItemType]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogItemSyncTypes")
    def catalog_item_sync_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CatalogItemType]]]]]:
        
        ...
    
    @catalog_item_sync_types.setter
    def catalog_item_sync_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CatalogItemType]]]]]): # -> None:
        ...
    


class ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgsDict(TypedDict):
    
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs:
    def __init__(__self__, *, roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ResourcePolicyArgsDict(TypedDict):
    
    filter: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourcePolicyArgs:
    def __init__(__self__, *, filter: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    


class StopOnDisconnectConfigurationArgsDict(TypedDict):
    
    grace_period_minutes: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, StopOnDisconnectEnableStatus]]]


@pulumi.input_type
class StopOnDisconnectConfigurationArgs:
    def __init__(__self__, *, grace_period_minutes: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, StopOnDisconnectEnableStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gracePeriodMinutes")
    def grace_period_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @grace_period_minutes.setter
    def grace_period_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, StopOnDisconnectEnableStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, StopOnDisconnectEnableStatus]]]): # -> None:
        ...
    


class UserRoleAssignmentArgsDict(TypedDict):
    
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserRoleAssignmentArgs:
    def __init__(__self__, *, roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


