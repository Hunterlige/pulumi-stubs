

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPolicyEntryArgs', 'AccessPolicyEntryArgsDict', 'ActionArgs', 'ActionArgsDict', 'IPRuleArgs', 'IPRuleArgsDict', 'KeyAttributesArgs', 'KeyAttributesArgsDict', 'KeyPropertiesArgs', 'KeyPropertiesArgsDict', 'KeyReleasePolicyArgs', 'KeyReleasePolicyArgsDict', 'KeyRotationPolicyAttributesArgs', 'KeyRotationPolicyAttributesArgsDict', 'LifetimeActionArgs', 'LifetimeActionArgsDict', 'MHSMGeoReplicatedRegionArgs', 'MHSMGeoReplicatedRegionArgsDict', 'MHSMIPRuleArgs', 'MHSMIPRuleArgsDict', 'MHSMNetworkRuleSetArgs', 'MHSMNetworkRuleSetArgsDict', 'MHSMPrivateLinkServiceConnectionStateArgs', 'MHSMPrivateLinkServiceConnectionStateArgsDict', 'MHSMVirtualNetworkRuleArgs', 'MHSMVirtualNetworkRuleArgsDict', 'ManagedHsmPropertiesArgs', 'ManagedHsmPropertiesArgsDict', 'ManagedHsmSkuArgs', 'ManagedHsmSkuArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'NetworkRuleSetArgs', 'NetworkRuleSetArgsDict', 'PermissionsArgs', 'PermissionsArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'RotationPolicyArgs', 'RotationPolicyArgsDict', 'SecretAttributesArgs', 'SecretAttributesArgsDict', 'SecretPropertiesArgs', 'SecretPropertiesArgsDict', 'SkuArgs', 'SkuArgsDict', 'TriggerArgs', 'TriggerArgsDict', 'VaultPropertiesArgs', 'VaultPropertiesArgsDict', 'VirtualNetworkRuleArgs', 'VirtualNetworkRuleArgsDict']
class AccessPolicyEntryArgsDict(TypedDict):
    
    object_id: pulumi.Input[_builtins.str]
    permissions: pulumi.Input[PermissionsArgsDict]
    tenant_id: pulumi.Input[_builtins.str]
    application_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AccessPolicyEntryArgs:
    def __init__(__self__, *, object_id: pulumi.Input[_builtins.str], permissions: pulumi.Input[PermissionsArgs], tenant_id: pulumi.Input[_builtins.str], application_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[PermissionsArgs]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: pulumi.Input[PermissionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ActionArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[KeyRotationPolicyActionType]]


@pulumi.input_type
class ActionArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[KeyRotationPolicyActionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[KeyRotationPolicyActionType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[KeyRotationPolicyActionType]]): # -> None:
        ...
    


class IPRuleArgsDict(TypedDict):
    
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class IPRuleArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class KeyAttributesArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expires: NotRequired[pulumi.Input[_builtins.float]]
    exportable: NotRequired[pulumi.Input[_builtins.bool]]
    not_before: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class KeyAttributesArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expires: Optional[pulumi.Input[_builtins.float]] = ..., exportable: Optional[pulumi.Input[_builtins.bool]] = ..., not_before: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @expires.setter
    def expires(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exportable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exportable.setter
    def exportable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class KeyPropertiesArgsDict(TypedDict):
    
    attributes: NotRequired[pulumi.Input[KeyAttributesArgsDict]]
    curve_name: NotRequired[pulumi.Input[Union[_builtins.str, JsonWebKeyCurveName]]]
    key_ops: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, JsonWebKeyOperation]]]]]
    key_size: NotRequired[pulumi.Input[_builtins.int]]
    kty: NotRequired[pulumi.Input[Union[_builtins.str, JsonWebKeyType]]]
    release_policy: NotRequired[pulumi.Input[KeyReleasePolicyArgsDict]]
    rotation_policy: NotRequired[pulumi.Input[RotationPolicyArgsDict]]


@pulumi.input_type
class KeyPropertiesArgs:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[KeyAttributesArgs]] = ..., curve_name: Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyCurveName]]] = ..., key_ops: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, JsonWebKeyOperation]]]]] = ..., key_size: Optional[pulumi.Input[_builtins.int]] = ..., kty: Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyType]]] = ..., release_policy: Optional[pulumi.Input[KeyReleasePolicyArgs]] = ..., rotation_policy: Optional[pulumi.Input[RotationPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[KeyAttributesArgs]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[KeyAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="curveName")
    def curve_name(self) -> Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyCurveName]]]:
        
        ...
    
    @curve_name.setter
    def curve_name(self, value: Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyCurveName]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyOps")
    def key_ops(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, JsonWebKeyOperation]]]]]:
        ...
    
    @key_ops.setter
    def key_ops(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, JsonWebKeyOperation]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_size.setter
    def key_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kty(self) -> Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyType]]]:
        
        ...
    
    @kty.setter
    def kty(self, value: Optional[pulumi.Input[Union[_builtins.str, JsonWebKeyType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releasePolicy")
    def release_policy(self) -> Optional[pulumi.Input[KeyReleasePolicyArgs]]:
        
        ...
    
    @release_policy.setter
    def release_policy(self, value: Optional[pulumi.Input[KeyReleasePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPolicy")
    def rotation_policy(self) -> Optional[pulumi.Input[RotationPolicyArgs]]:
        
        ...
    
    @rotation_policy.setter
    def rotation_policy(self, value: Optional[pulumi.Input[RotationPolicyArgs]]): # -> None:
        ...
    


class KeyReleasePolicyArgsDict(TypedDict):
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyReleasePolicyArgs:
    def __init__(__self__, *, content_type: Optional[pulumi.Input[_builtins.str]] = ..., data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyRotationPolicyAttributesArgsDict(TypedDict):
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyRotationPolicyAttributesArgs:
    def __init__(__self__, *, expiry_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LifetimeActionArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[ActionArgsDict]]
    trigger: NotRequired[pulumi.Input[TriggerArgsDict]]


@pulumi.input_type
class LifetimeActionArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[ActionArgs]] = ..., trigger: Optional[pulumi.Input[TriggerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[ActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[ActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[TriggerArgs]]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[TriggerArgs]]): # -> None:
        ...
    


class MHSMGeoReplicatedRegionArgsDict(TypedDict):
    
    is_primary: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MHSMGeoReplicatedRegionArgs:
    def __init__(__self__, *, is_primary: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_primary.setter
    def is_primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MHSMIPRuleArgsDict(TypedDict):
    
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class MHSMIPRuleArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MHSMNetworkRuleSetArgsDict(TypedDict):
    
    bypass: NotRequired[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]
    default_action: NotRequired[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[MHSMIPRuleArgsDict]]]]
    virtual_network_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[MHSMVirtualNetworkRuleArgsDict]]]]


@pulumi.input_type
class MHSMNetworkRuleSetArgs:
    def __init__(__self__, *, bypass: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]] = ..., default_action: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMIPRuleArgs]]]] = ..., virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMVirtualNetworkRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bypass(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]:
        
        ...
    
    @bypass.setter
    def bypass(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]:
        
        ...
    
    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MHSMIPRuleArgs]]]]:
        
        ...
    
    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMIPRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MHSMVirtualNetworkRuleArgs]]]]:
        
        ...
    
    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMVirtualNetworkRuleArgs]]]]): # -> None:
        ...
    


class MHSMPrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[Union[_builtins.str, ActionsRequired]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class MHSMPrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class MHSMVirtualNetworkRuleArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class MHSMVirtualNetworkRuleArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedHsmPropertiesArgsDict(TypedDict):
    
    create_mode: NotRequired[pulumi.Input[CreateMode]]
    enable_purge_protection: NotRequired[pulumi.Input[_builtins.bool]]
    enable_soft_delete: NotRequired[pulumi.Input[_builtins.bool]]
    initial_admin_object_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network_acls: NotRequired[pulumi.Input[MHSMNetworkRuleSetArgsDict]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[MHSMGeoReplicatedRegionArgsDict]]]]
    soft_delete_retention_in_days: NotRequired[pulumi.Input[_builtins.int]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedHsmPropertiesArgs:
    def __init__(__self__, *, create_mode: Optional[pulumi.Input[CreateMode]] = ..., enable_purge_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enable_soft_delete: Optional[pulumi.Input[_builtins.bool]] = ..., initial_admin_object_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_acls: Optional[pulumi.Input[MHSMNetworkRuleSetArgs]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMGeoReplicatedRegionArgs]]]] = ..., soft_delete_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[CreateMode]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[CreateMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_purge_protection.setter
    def enable_purge_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSoftDelete")
    def enable_soft_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_soft_delete.setter
    def enable_soft_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialAdminObjectIds")
    def initial_admin_object_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @initial_admin_object_ids.setter
    def initial_admin_object_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input[MHSMNetworkRuleSetArgs]]:
        
        ...
    
    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input[MHSMNetworkRuleSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MHSMGeoReplicatedRegionArgs]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MHSMGeoReplicatedRegionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @soft_delete_retention_in_days.setter
    def soft_delete_retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedHsmSkuArgsDict(TypedDict):
    
    family: pulumi.Input[Union[_builtins.str, ManagedHsmSkuFamily]]
    name: pulumi.Input[ManagedHsmSkuName]


@pulumi.input_type
class ManagedHsmSkuArgs:
    def __init__(__self__, *, family: pulumi.Input[Union[_builtins.str, ManagedHsmSkuFamily]], name: pulumi.Input[ManagedHsmSkuName]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Input[Union[_builtins.str, ManagedHsmSkuFamily]]:
        
        ...
    
    @family.setter
    def family(self, value: pulumi.Input[Union[_builtins.str, ManagedHsmSkuFamily]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[ManagedHsmSkuName]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[ManagedHsmSkuName]): # -> None:
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
    


class NetworkRuleSetArgsDict(TypedDict):
    
    bypass: NotRequired[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]
    default_action: NotRequired[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPRuleArgsDict]]]]
    virtual_network_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgsDict]]]]


@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(__self__, *, bypass: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]] = ..., default_action: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]] = ..., virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bypass(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]:
        
        ...
    
    @bypass.setter
    def bypass(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleBypassOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]:
        
        ...
    
    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleAction]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]:
        
        ...
    
    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]]:
        
        ...
    
    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]]): # -> None:
        ...
    


class PermissionsArgsDict(TypedDict):
    
    certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CertificatePermissions]]]]]
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KeyPermissions]]]]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SecretPermissions]]]]]
    storage: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StoragePermissions]]]]]


@pulumi.input_type
class PermissionsArgs:
    def __init__(__self__, *, certificates: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CertificatePermissions]]]]] = ..., keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KeyPermissions]]]]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SecretPermissions]]]]] = ..., storage: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StoragePermissions]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CertificatePermissions]]]]]:
        
        ...
    
    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CertificatePermissions]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KeyPermissions]]]]]:
        
        ...
    
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KeyPermissions]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SecretPermissions]]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SecretPermissions]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StoragePermissions]]]]]:
        
        ...
    
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, StoragePermissions]]]]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[Union[_builtins.str, ActionsRequired]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class RotationPolicyArgsDict(TypedDict):
    attributes: NotRequired[pulumi.Input[KeyRotationPolicyAttributesArgsDict]]
    lifetime_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[LifetimeActionArgsDict]]]]


@pulumi.input_type
class RotationPolicyArgs:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[KeyRotationPolicyAttributesArgs]] = ..., lifetime_actions: Optional[pulumi.Input[Sequence[pulumi.Input[LifetimeActionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[KeyRotationPolicyAttributesArgs]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[KeyRotationPolicyAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifetimeActions")
    def lifetime_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LifetimeActionArgs]]]]:
        
        ...
    
    @lifetime_actions.setter
    def lifetime_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LifetimeActionArgs]]]]): # -> None:
        ...
    


class SecretAttributesArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expires: NotRequired[pulumi.Input[_builtins.int]]
    not_before: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SecretAttributesArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expires: Optional[pulumi.Input[_builtins.int]] = ..., not_before: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expires.setter
    def expires(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SecretPropertiesArgsDict(TypedDict):
    
    attributes: NotRequired[pulumi.Input[SecretAttributesArgsDict]]
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretPropertiesArgs:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[SecretAttributesArgs]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[SecretAttributesArgs]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[SecretAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    family: pulumi.Input[Union[_builtins.str, SkuFamily]]
    name: pulumi.Input[SkuName]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, family: pulumi.Input[Union[_builtins.str, SkuFamily]], name: pulumi.Input[SkuName]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Input[Union[_builtins.str, SkuFamily]]:
        
        ...
    
    @family.setter
    def family(self, value: pulumi.Input[Union[_builtins.str, SkuFamily]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[SkuName]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[SkuName]): # -> None:
        ...
    


class TriggerArgsDict(TypedDict):
    time_after_create: NotRequired[pulumi.Input[_builtins.str]]
    time_before_expiry: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TriggerArgs:
    def __init__(__self__, *, time_after_create: Optional[pulumi.Input[_builtins.str]] = ..., time_before_expiry: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeAfterCreate")
    def time_after_create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_after_create.setter
    def time_after_create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeBeforeExpiry")
    def time_before_expiry(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_before_expiry.setter
    def time_before_expiry(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VaultPropertiesArgsDict(TypedDict):
    
    sku: pulumi.Input[SkuArgsDict]
    tenant_id: pulumi.Input[_builtins.str]
    access_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessPolicyEntryArgsDict]]]]
    create_mode: NotRequired[pulumi.Input[CreateMode]]
    enable_purge_protection: NotRequired[pulumi.Input[_builtins.bool]]
    enable_rbac_authorization: NotRequired[pulumi.Input[_builtins.bool]]
    enable_soft_delete: NotRequired[pulumi.Input[_builtins.bool]]
    enabled_for_deployment: NotRequired[pulumi.Input[_builtins.bool]]
    enabled_for_disk_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    enabled_for_template_deployment: NotRequired[pulumi.Input[_builtins.bool]]
    network_acls: NotRequired[pulumi.Input[NetworkRuleSetArgsDict]]
    public_network_access: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_in_days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VaultPropertiesArgs:
    def __init__(__self__, *, sku: pulumi.Input[SkuArgs], tenant_id: pulumi.Input[_builtins.str], access_policies: Optional[pulumi.Input[Sequence[pulumi.Input[AccessPolicyEntryArgs]]]] = ..., create_mode: Optional[pulumi.Input[CreateMode]] = ..., enable_purge_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enable_rbac_authorization: Optional[pulumi.Input[_builtins.bool]] = ..., enable_soft_delete: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_for_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_for_disk_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_for_template_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., network_acls: Optional[pulumi.Input[NetworkRuleSetArgs]] = ..., public_network_access: Optional[pulumi.Input[_builtins.str]] = ..., soft_delete_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessPolicyEntryArgs]]]]:
        
        ...
    
    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessPolicyEntryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[CreateMode]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[CreateMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_purge_protection.setter
    def enable_purge_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRbacAuthorization")
    def enable_rbac_authorization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_rbac_authorization.setter
    def enable_rbac_authorization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSoftDelete")
    def enable_soft_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_soft_delete.setter
    def enable_soft_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForDeployment")
    def enabled_for_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled_for_deployment.setter
    def enabled_for_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled_for_disk_encryption.setter
    def enabled_for_disk_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled_for_template_deployment.setter
    def enabled_for_template_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input[NetworkRuleSetArgs]]:
        
        ...
    
    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input[NetworkRuleSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @soft_delete_retention_in_days.setter
    def soft_delete_retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VirtualNetworkRuleArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    ignore_missing_vnet_service_endpoint: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


