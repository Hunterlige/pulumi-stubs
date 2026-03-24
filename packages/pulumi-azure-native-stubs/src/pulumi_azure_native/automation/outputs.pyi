

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
__all__ = ['AdvancedScheduleMonthlyOccurrenceResponse', 'AdvancedScheduleResponse', 'AzureQueryPropertiesResponse', 'ConnectionTypeAssociationPropertyResponse', 'ContentHashResponse', 'ContentLinkResponse', 'ContentSourceResponse', 'DeletedRunbookResponse', 'DscConfigurationAssociationPropertyResponse', 'DscConfigurationParameterResponse', 'EncryptionPropertiesResponse', 'EncryptionPropertiesResponseIdentity', 'ErrorResponseResponse', 'FieldDefinitionResponse', 'IdentityResponse', 'KeyResponse', 'KeyVaultPropertiesResponse', 'LinuxPropertiesResponse', 'ModuleErrorInfoResponse', 'NonAzureQueryPropertiesResponse', 'PackageErrorInfoResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointPropertyResponse', 'PrivateLinkServiceConnectionStatePropertyResponse', 'RunAsCredentialAssociationPropertyResponse', 'RunbookAssociationPropertyResponse', 'RunbookDraftResponse', 'RunbookParameterResponse', 'SUCSchedulePropertiesResponse', 'ScheduleAssociationPropertyResponse', 'SkuResponse', 'SoftwareUpdateConfigurationTasksResponse', 'SystemDataResponse', 'TagSettingsPropertiesResponse', 'TargetPropertiesResponse', 'TaskPropertiesResponse', 'UpdateConfigurationResponse', 'UserAssignedIdentitiesPropertiesResponse', 'WindowsPropertiesResponse']
@pulumi.output_type
class AdvancedScheduleMonthlyOccurrenceResponse(dict):
    
    def __init__(__self__, *, day: Optional[_builtins.str] = ..., occurrence: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def occurrence(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AdvancedScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, month_days: Optional[Sequence[_builtins.int]] = ..., monthly_occurrences: Optional[Sequence[outputs.AdvancedScheduleMonthlyOccurrenceResponse]] = ..., week_days: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[Sequence[outputs.AdvancedScheduleMonthlyOccurrenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AzureQueryPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, locations: Optional[Sequence[_builtins.str]] = ..., scope: Optional[Sequence[_builtins.str]] = ..., tag_settings: Optional[outputs.TagSettingsPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional[outputs.TagSettingsPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ConnectionTypeAssociationPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContentHashResponse(dict):
    
    def __init__(__self__, *, algorithm: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ContentLinkResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_hash: Optional[outputs.ContentHashResponse] = ..., uri: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[outputs.ContentHashResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContentSourceResponse(dict):
    
    def __init__(__self__, *, hash: Optional[outputs.ContentHashResponse] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hash(self) -> Optional[outputs.ContentHashResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeletedRunbookResponse(dict):
    
    def __init__(__self__, *, creation_time: Optional[_builtins.str] = ..., deletion_time: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., runbook_id: Optional[_builtins.str] = ..., runbook_type: Optional[_builtins.str] = ..., runtime: Optional[_builtins.str] = ..., runtime_environment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionTime")
    def deletion_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runbookId")
    def runbook_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runbookType")
    def runbook_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DscConfigurationAssociationPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DscConfigurationParameterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: Optional[_builtins.str] = ..., is_mandatory: Optional[_builtins.bool] = ..., position: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMandatory")
    def is_mandatory(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[outputs.EncryptionPropertiesResponseIdentity] = ..., key_source: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.EncryptionPropertiesResponseIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class EncryptionPropertiesResponseIdentity(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_assigned_identity: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class ErrorResponseResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FieldDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, is_encrypted: Optional[_builtins.bool] = ..., is_optional: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOptional")
    def is_optional(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentitiesPropertiesResponse]] = ...) -> None:
        
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
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentitiesPropertiesResponse]]:
        
        ...
    


@pulumi.output_type
class KeyResponse(dict):
    
    def __init__(__self__, *, key_name: _builtins.str, permissions: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: Optional[_builtins.str] = ..., key_version: Optional[_builtins.str] = ..., keyvault_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyvaultUri")
    def keyvault_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LinuxPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_package_name_masks: Optional[Sequence[_builtins.str]] = ..., included_package_classifications: Optional[_builtins.str] = ..., included_package_name_masks: Optional[Sequence[_builtins.str]] = ..., reboot_setting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPackageNameMasks")
    def excluded_package_name_masks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPackageClassifications")
    def included_package_classifications(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPackageNameMasks")
    def included_package_name_masks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ModuleErrorInfoResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NonAzureQueryPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_alias: Optional[_builtins.str] = ..., workspace_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PackageErrorInfoResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointPropertyResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointPropertyResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStatePropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
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
class RunAsCredentialAssociationPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RunbookAssociationPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RunbookDraftResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time: Optional[_builtins.str] = ..., draft_content_link: Optional[outputs.ContentLinkResponse] = ..., in_edit: Optional[_builtins.bool] = ..., last_modified_time: Optional[_builtins.str] = ..., output_types: Optional[Sequence[_builtins.str]] = ..., parameters: Optional[Mapping[str, outputs.RunbookParameterResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="draftContentLink")
    def draft_content_link(self) -> Optional[outputs.ContentLinkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inEdit")
    def in_edit(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputTypes")
    def output_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.RunbookParameterResponse]]:
        
        ...
    


@pulumi.output_type
class RunbookParameterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: Optional[_builtins.str] = ..., is_mandatory: Optional[_builtins.bool] = ..., position: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMandatory")
    def is_mandatory(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SUCSchedulePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_time_offset_minutes: _builtins.float, advanced_schedule: Optional[outputs.AdvancedScheduleResponse] = ..., creation_time: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., expiry_time_offset_minutes: Optional[_builtins.float] = ..., frequency: Optional[_builtins.str] = ..., interval: Optional[_builtins.float] = ..., is_enabled: Optional[_builtins.bool] = ..., last_modified_time: Optional[_builtins.str] = ..., next_run: Optional[_builtins.str] = ..., next_run_offset_minutes: Optional[_builtins.float] = ..., start_time: Optional[_builtins.str] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional[outputs.AdvancedScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScheduleAssociationPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SoftwareUpdateConfigurationTasksResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, post_task: Optional[outputs.TaskPropertiesResponse] = ..., pre_task: Optional[outputs.TaskPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postTask")
    def post_task(self) -> Optional[outputs.TaskPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preTask")
    def pre_task(self) -> Optional[outputs.TaskPropertiesResponse]:
        
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
class TagSettingsPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter_operator: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, Sequence[_builtins.str]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[_builtins.str]]]:
        
        ...
    


@pulumi.output_type
class TargetPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_queries: Optional[Sequence[outputs.AzureQueryPropertiesResponse]] = ..., non_azure_queries: Optional[Sequence[outputs.NonAzureQueryPropertiesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureQueries")
    def azure_queries(self) -> Optional[Sequence[outputs.AzureQueryPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAzureQueries")
    def non_azure_queries(self) -> Optional[Sequence[outputs.NonAzureQueryPropertiesResponse]]:
        
        ...
    


@pulumi.output_type
class TaskPropertiesResponse(dict):
    
    def __init__(__self__, *, parameters: Optional[Mapping[str, _builtins.str]] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UpdateConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operating_system: _builtins.str, azure_virtual_machines: Optional[Sequence[_builtins.str]] = ..., duration: Optional[_builtins.str] = ..., linux: Optional[outputs.LinuxPropertiesResponse] = ..., non_azure_computer_names: Optional[Sequence[_builtins.str]] = ..., targets: Optional[outputs.TargetPropertiesResponse] = ..., windows: Optional[outputs.WindowsPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVirtualMachines")
    def azure_virtual_machines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def linux(self) -> Optional[outputs.LinuxPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAzureComputerNames")
    def non_azure_computer_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[outputs.TargetPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def windows(self) -> Optional[outputs.WindowsPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentitiesPropertiesResponse(dict):
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
    


@pulumi.output_type
class WindowsPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_kb_numbers: Optional[Sequence[_builtins.str]] = ..., included_kb_numbers: Optional[Sequence[_builtins.str]] = ..., included_update_classifications: Optional[_builtins.str] = ..., reboot_setting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedKbNumbers")
    def excluded_kb_numbers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedKbNumbers")
    def included_kb_numbers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedUpdateClassifications")
    def included_update_classifications(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]:
        
        ...
    


