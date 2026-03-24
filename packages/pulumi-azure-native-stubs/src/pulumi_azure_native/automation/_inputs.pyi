

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AdvancedScheduleMonthlyOccurrenceArgs', 'AdvancedScheduleMonthlyOccurrenceArgsDict', 'AdvancedScheduleArgs', 'AdvancedScheduleArgsDict', 'AzureQueryPropertiesArgs', 'AzureQueryPropertiesArgsDict', 'ConnectionTypeAssociationPropertyArgs', 'ConnectionTypeAssociationPropertyArgsDict', 'ContentHashArgs', 'ContentHashArgsDict', 'ContentLinkArgs', 'ContentLinkArgsDict', 'ContentSourceArgs', 'ContentSourceArgsDict', 'DscConfigurationAssociationPropertyArgs', 'DscConfigurationAssociationPropertyArgsDict', 'DscConfigurationParameterArgs', 'DscConfigurationParameterArgsDict', 'EncryptionPropertiesIdentityArgs', 'EncryptionPropertiesIdentityArgsDict', 'EncryptionPropertiesArgs', 'EncryptionPropertiesArgsDict', 'ErrorResponseArgs', 'ErrorResponseArgsDict', 'FieldDefinitionArgs', 'FieldDefinitionArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict', 'LinuxPropertiesArgs', 'LinuxPropertiesArgsDict', 'NonAzureQueryPropertiesArgs', 'NonAzureQueryPropertiesArgsDict', 'PrivateEndpointPropertyArgs', 'PrivateEndpointPropertyArgsDict', 'PrivateLinkServiceConnectionStatePropertyArgs', 'PrivateLinkServiceConnectionStatePropertyArgsDict', 'RunAsCredentialAssociationPropertyArgs', 'RunAsCredentialAssociationPropertyArgsDict', 'RunbookAssociationPropertyArgs', 'RunbookAssociationPropertyArgsDict', 'RunbookDraftArgs', 'RunbookDraftArgsDict', 'RunbookParameterArgs', 'RunbookParameterArgsDict', 'SUCSchedulePropertiesArgs', 'SUCSchedulePropertiesArgsDict', 'ScheduleAssociationPropertyArgs', 'ScheduleAssociationPropertyArgsDict', 'SkuArgs', 'SkuArgsDict', 'SoftwareUpdateConfigurationTasksArgs', 'SoftwareUpdateConfigurationTasksArgsDict', 'SourceControlSecurityTokenPropertiesArgs', 'SourceControlSecurityTokenPropertiesArgsDict', 'TagSettingsPropertiesArgs', 'TagSettingsPropertiesArgsDict', 'TargetPropertiesArgs', 'TargetPropertiesArgsDict', 'TaskPropertiesArgs', 'TaskPropertiesArgsDict', 'TrackedResourceArgs', 'TrackedResourceArgsDict', 'UpdateConfigurationArgs', 'UpdateConfigurationArgsDict', 'WindowsPropertiesArgs', 'WindowsPropertiesArgsDict']
class AdvancedScheduleMonthlyOccurrenceArgsDict(TypedDict):
    
    day: NotRequired[pulumi.Input[Union[_builtins.str, ScheduleDay]]]
    occurrence: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AdvancedScheduleMonthlyOccurrenceArgs:
    def __init__(__self__, *, day: Optional[pulumi.Input[Union[_builtins.str, ScheduleDay]]] = ..., occurrence: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleDay]]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleDay]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def occurrence(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @occurrence.setter
    def occurrence(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AdvancedScheduleArgsDict(TypedDict):
    
    month_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    monthly_occurrences: NotRequired[pulumi.Input[Sequence[pulumi.Input[AdvancedScheduleMonthlyOccurrenceArgsDict]]]]
    week_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AdvancedScheduleArgs:
    def __init__(__self__, *, month_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., monthly_occurrences: Optional[pulumi.Input[Sequence[pulumi.Input[AdvancedScheduleMonthlyOccurrenceArgs]]]] = ..., week_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @month_days.setter
    def month_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AdvancedScheduleMonthlyOccurrenceArgs]]]]:
        
        ...
    
    @monthly_occurrences.setter
    def monthly_occurrences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AdvancedScheduleMonthlyOccurrenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @week_days.setter
    def week_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AzureQueryPropertiesArgsDict(TypedDict):
    
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    scope: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tag_settings: NotRequired[pulumi.Input[TagSettingsPropertiesArgsDict]]


@pulumi.input_type
class AzureQueryPropertiesArgs:
    def __init__(__self__, *, locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scope: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_settings: Optional[pulumi.Input[TagSettingsPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional[pulumi.Input[TagSettingsPropertiesArgs]]:
        
        ...
    
    @tag_settings.setter
    def tag_settings(self, value: Optional[pulumi.Input[TagSettingsPropertiesArgs]]): # -> None:
        ...
    


class ConnectionTypeAssociationPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionTypeAssociationPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContentHashArgsDict(TypedDict):
    
    algorithm: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContentHashArgs:
    def __init__(__self__, *, algorithm: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ContentLinkArgsDict(TypedDict):
    
    content_hash: NotRequired[pulumi.Input[ContentHashArgsDict]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContentLinkArgs:
    def __init__(__self__, *, content_hash: Optional[pulumi.Input[ContentHashArgs]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[pulumi.Input[ContentHashArgs]]:
        
        ...
    
    @content_hash.setter
    def content_hash(self, value: Optional[pulumi.Input[ContentHashArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContentSourceArgsDict(TypedDict):
    
    hash: NotRequired[pulumi.Input[ContentHashArgsDict]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ContentSourceType]]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContentSourceArgs:
    def __init__(__self__, *, hash: Optional[pulumi.Input[ContentHashArgs]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ContentSourceType]]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hash(self) -> Optional[pulumi.Input[ContentHashArgs]]:
        
        ...
    
    @hash.setter
    def hash(self, value: Optional[pulumi.Input[ContentHashArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ContentSourceType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ContentSourceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DscConfigurationAssociationPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DscConfigurationAssociationPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DscConfigurationParameterArgsDict(TypedDict):
    
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    is_mandatory: NotRequired[pulumi.Input[_builtins.bool]]
    position: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DscConfigurationParameterArgs:
    def __init__(__self__, *, default_value: Optional[pulumi.Input[_builtins.str]] = ..., is_mandatory: Optional[pulumi.Input[_builtins.bool]] = ..., position: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMandatory")
    def is_mandatory(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_mandatory.setter
    def is_mandatory(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @position.setter
    def position(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionPropertiesIdentityArgsDict(TypedDict):
    
    user_assigned_identity: NotRequired[Any]


@pulumi.input_type
class EncryptionPropertiesIdentityArgs:
    def __init__(__self__, *, user_assigned_identity: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[Any]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[Any]): # -> None:
        ...
    


class EncryptionPropertiesArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[EncryptionPropertiesIdentityArgsDict]]
    key_source: NotRequired[pulumi.Input[EncryptionKeySourceType]]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]


@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]] = ..., key_source: Optional[pulumi.Input[EncryptionKeySourceType]] = ..., key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[EncryptionPropertiesIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[EncryptionKeySourceType]]:
        
        ...
    
    @key_source.setter
    def key_source(self, value: Optional[pulumi.Input[EncryptionKeySourceType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]:
        
        ...
    
    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]): # -> None:
        ...
    


class ErrorResponseArgsDict(TypedDict):
    
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ErrorResponseArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FieldDefinitionArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    is_encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    is_optional: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FieldDefinitionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], is_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., is_optional: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_encrypted.setter
    def is_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOptional")
    def is_optional(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_optional.setter
    def is_optional(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class KeyVaultPropertiesArgsDict(TypedDict):
    
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]
    keyvault_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *, key_name: Optional[pulumi.Input[_builtins.str]] = ..., key_version: Optional[pulumi.Input[_builtins.str]] = ..., keyvault_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyvaultUri")
    def keyvault_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @keyvault_uri.setter
    def keyvault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LinuxPropertiesArgsDict(TypedDict):
    
    excluded_package_name_masks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_package_classifications: NotRequired[pulumi.Input[Union[_builtins.str, LinuxUpdateClasses]]]
    included_package_name_masks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    reboot_setting: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LinuxPropertiesArgs:
    def __init__(__self__, *, excluded_package_name_masks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., included_package_classifications: Optional[pulumi.Input[Union[_builtins.str, LinuxUpdateClasses]]] = ..., included_package_name_masks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reboot_setting: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPackageNameMasks")
    def excluded_package_name_masks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_package_name_masks.setter
    def excluded_package_name_masks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPackageClassifications")
    def included_package_classifications(self) -> Optional[pulumi.Input[Union[_builtins.str, LinuxUpdateClasses]]]:
        
        ...
    
    @included_package_classifications.setter
    def included_package_classifications(self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxUpdateClasses]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPackageNameMasks")
    def included_package_name_masks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @included_package_name_masks.setter
    def included_package_name_masks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reboot_setting.setter
    def reboot_setting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NonAzureQueryPropertiesArgsDict(TypedDict):
    
    function_alias: NotRequired[pulumi.Input[_builtins.str]]
    workspace_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NonAzureQueryPropertiesArgs:
    def __init__(__self__, *, function_alias: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_alias.setter
    def function_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateEndpointPropertyArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RunAsCredentialAssociationPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RunAsCredentialAssociationPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RunbookAssociationPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RunbookAssociationPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RunbookDraftArgsDict(TypedDict):
    creation_time: NotRequired[pulumi.Input[_builtins.str]]
    draft_content_link: NotRequired[pulumi.Input[ContentLinkArgsDict]]
    in_edit: NotRequired[pulumi.Input[_builtins.bool]]
    last_modified_time: NotRequired[pulumi.Input[_builtins.str]]
    output_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[RunbookParameterArgsDict]]]]


@pulumi.input_type
class RunbookDraftArgs:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., draft_content_link: Optional[pulumi.Input[ContentLinkArgs]] = ..., in_edit: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., output_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[RunbookParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="draftContentLink")
    def draft_content_link(self) -> Optional[pulumi.Input[ContentLinkArgs]]:
        
        ...
    
    @draft_content_link.setter
    def draft_content_link(self, value: Optional[pulumi.Input[ContentLinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inEdit")
    def in_edit(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @in_edit.setter
    def in_edit(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputTypes")
    def output_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @output_types.setter
    def output_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[RunbookParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[RunbookParameterArgs]]]]): # -> None:
        ...
    


class RunbookParameterArgsDict(TypedDict):
    
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    is_mandatory: NotRequired[pulumi.Input[_builtins.bool]]
    position: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RunbookParameterArgs:
    def __init__(__self__, *, default_value: Optional[pulumi.Input[_builtins.str]] = ..., is_mandatory: Optional[pulumi.Input[_builtins.bool]] = ..., position: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMandatory")
    def is_mandatory(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_mandatory.setter
    def is_mandatory(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @position.setter
    def position(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SUCSchedulePropertiesArgsDict(TypedDict):
    
    advanced_schedule: NotRequired[pulumi.Input[AdvancedScheduleArgsDict]]
    creation_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time_offset_minutes: NotRequired[pulumi.Input[_builtins.float]]
    frequency: NotRequired[pulumi.Input[Union[_builtins.str, ScheduleFrequency]]]
    interval: NotRequired[pulumi.Input[_builtins.float]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    last_modified_time: NotRequired[pulumi.Input[_builtins.str]]
    next_run: NotRequired[pulumi.Input[_builtins.str]]
    next_run_offset_minutes: NotRequired[pulumi.Input[_builtins.float]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SUCSchedulePropertiesArgs:
    def __init__(__self__, *, advanced_schedule: Optional[pulumi.Input[AdvancedScheduleArgs]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., expiry_time: Optional[pulumi.Input[_builtins.str]] = ..., expiry_time_offset_minutes: Optional[pulumi.Input[_builtins.float]] = ..., frequency: Optional[pulumi.Input[Union[_builtins.str, ScheduleFrequency]]] = ..., interval: Optional[pulumi.Input[_builtins.float]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., next_run: Optional[pulumi.Input[_builtins.str]] = ..., next_run_offset_minutes: Optional[pulumi.Input[_builtins.float]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional[pulumi.Input[AdvancedScheduleArgs]]:
        
        ...
    
    @advanced_schedule.setter
    def advanced_schedule(self, value: Optional[pulumi.Input[AdvancedScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @expiry_time_offset_minutes.setter
    def expiry_time_offset_minutes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleFrequency]]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleFrequency]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_run.setter
    def next_run(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @next_run_offset_minutes.setter
    def next_run_offset_minutes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScheduleAssociationPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScheduleAssociationPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, SkuNameEnum]]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, SkuNameEnum]], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuNameEnum]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuNameEnum]]): # -> None:
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
    


class SoftwareUpdateConfigurationTasksArgsDict(TypedDict):
    
    post_task: NotRequired[pulumi.Input[TaskPropertiesArgsDict]]
    pre_task: NotRequired[pulumi.Input[TaskPropertiesArgsDict]]


@pulumi.input_type
class SoftwareUpdateConfigurationTasksArgs:
    def __init__(__self__, *, post_task: Optional[pulumi.Input[TaskPropertiesArgs]] = ..., pre_task: Optional[pulumi.Input[TaskPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postTask")
    def post_task(self) -> Optional[pulumi.Input[TaskPropertiesArgs]]:
        
        ...
    
    @post_task.setter
    def post_task(self, value: Optional[pulumi.Input[TaskPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTask")
    def pre_task(self) -> Optional[pulumi.Input[TaskPropertiesArgs]]:
        
        ...
    
    @pre_task.setter
    def pre_task(self, value: Optional[pulumi.Input[TaskPropertiesArgs]]): # -> None:
        ...
    


class SourceControlSecurityTokenPropertiesArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]
    token_type: NotRequired[pulumi.Input[Union[_builtins.str, TokenType]]]


@pulumi.input_type
class SourceControlSecurityTokenPropertiesArgs:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ..., token_type: Optional[pulumi.Input[Union[_builtins.str, TokenType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenType")
    def token_type(self) -> Optional[pulumi.Input[Union[_builtins.str, TokenType]]]:
        
        ...
    
    @token_type.setter
    def token_type(self, value: Optional[pulumi.Input[Union[_builtins.str, TokenType]]]): # -> None:
        ...
    


class TagSettingsPropertiesArgsDict(TypedDict):
    
    filter_operator: NotRequired[pulumi.Input[TagOperators]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]]


@pulumi.input_type
class TagSettingsPropertiesArgs:
    def __init__(__self__, *, filter_operator: Optional[pulumi.Input[TagOperators]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[pulumi.Input[TagOperators]]:
        
        ...
    
    @filter_operator.setter
    def filter_operator(self, value: Optional[pulumi.Input[TagOperators]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    


class TargetPropertiesArgsDict(TypedDict):
    
    azure_queries: NotRequired[pulumi.Input[Sequence[pulumi.Input[AzureQueryPropertiesArgsDict]]]]
    non_azure_queries: NotRequired[pulumi.Input[Sequence[pulumi.Input[NonAzureQueryPropertiesArgsDict]]]]


@pulumi.input_type
class TargetPropertiesArgs:
    def __init__(__self__, *, azure_queries: Optional[pulumi.Input[Sequence[pulumi.Input[AzureQueryPropertiesArgs]]]] = ..., non_azure_queries: Optional[pulumi.Input[Sequence[pulumi.Input[NonAzureQueryPropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureQueries")
    def azure_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureQueryPropertiesArgs]]]]:
        
        ...
    
    @azure_queries.setter
    def azure_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureQueryPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAzureQueries")
    def non_azure_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NonAzureQueryPropertiesArgs]]]]:
        
        ...
    
    @non_azure_queries.setter
    def non_azure_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NonAzureQueryPropertiesArgs]]]]): # -> None:
        ...
    


class TaskPropertiesArgsDict(TypedDict):
    
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    source: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskPropertiesArgs:
    def __init__(__self__, *, parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrackedResourceArgsDict(TypedDict):
    
    location: pulumi.Input[_builtins.str]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TrackedResourceArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UpdateConfigurationArgsDict(TypedDict):
    
    operating_system: pulumi.Input[OperatingSystemType]
    azure_virtual_machines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    duration: NotRequired[pulumi.Input[_builtins.str]]
    linux: NotRequired[pulumi.Input[LinuxPropertiesArgsDict]]
    non_azure_computer_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    targets: NotRequired[pulumi.Input[TargetPropertiesArgsDict]]
    windows: NotRequired[pulumi.Input[WindowsPropertiesArgsDict]]


@pulumi.input_type
class UpdateConfigurationArgs:
    def __init__(__self__, *, operating_system: pulumi.Input[OperatingSystemType], azure_virtual_machines: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., duration: Optional[pulumi.Input[_builtins.str]] = ..., linux: Optional[pulumi.Input[LinuxPropertiesArgs]] = ..., non_azure_computer_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., targets: Optional[pulumi.Input[TargetPropertiesArgs]] = ..., windows: Optional[pulumi.Input[WindowsPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Input[OperatingSystemType]:
        
        ...
    
    @operating_system.setter
    def operating_system(self, value: pulumi.Input[OperatingSystemType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVirtualMachines")
    def azure_virtual_machines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @azure_virtual_machines.setter
    def azure_virtual_machines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def linux(self) -> Optional[pulumi.Input[LinuxPropertiesArgs]]:
        
        ...
    
    @linux.setter
    def linux(self, value: Optional[pulumi.Input[LinuxPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAzureComputerNames")
    def non_azure_computer_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @non_azure_computer_names.setter
    def non_azure_computer_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[TargetPropertiesArgs]]:
        
        ...
    
    @targets.setter
    def targets(self, value: Optional[pulumi.Input[TargetPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def windows(self) -> Optional[pulumi.Input[WindowsPropertiesArgs]]:
        
        ...
    
    @windows.setter
    def windows(self, value: Optional[pulumi.Input[WindowsPropertiesArgs]]): # -> None:
        ...
    


class WindowsPropertiesArgsDict(TypedDict):
    
    excluded_kb_numbers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_kb_numbers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_update_classifications: NotRequired[pulumi.Input[Union[_builtins.str, WindowsUpdateClasses]]]
    reboot_setting: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WindowsPropertiesArgs:
    def __init__(__self__, *, excluded_kb_numbers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., included_kb_numbers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., included_update_classifications: Optional[pulumi.Input[Union[_builtins.str, WindowsUpdateClasses]]] = ..., reboot_setting: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedKbNumbers")
    def excluded_kb_numbers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_kb_numbers.setter
    def excluded_kb_numbers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedKbNumbers")
    def included_kb_numbers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @included_kb_numbers.setter
    def included_kb_numbers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedUpdateClassifications")
    def included_update_classifications(self) -> Optional[pulumi.Input[Union[_builtins.str, WindowsUpdateClasses]]]:
        
        ...
    
    @included_update_classifications.setter
    def included_update_classifications(self, value: Optional[pulumi.Input[Union[_builtins.str, WindowsUpdateClasses]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reboot_setting.setter
    def reboot_setting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


