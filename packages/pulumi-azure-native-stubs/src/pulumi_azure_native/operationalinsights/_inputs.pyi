

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterSkuArgs', 'ClusterSkuArgsDict', 'ColumnArgs', 'ColumnArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict', 'LogAnalyticsQueryPackQueryPropertiesRelatedArgs', ..., 'MachineReferenceWithHintsArgs', 'MachineReferenceWithHintsArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'RestoredLogsArgs', 'RestoredLogsArgsDict', 'RuleDefinitionArgs', 'RuleDefinitionArgsDict', 'SchemaArgs', 'SchemaArgsDict', 'SearchResultsArgs', 'SearchResultsArgsDict', 'StorageAccountArgs', 'StorageAccountArgsDict', 'TagArgs', 'TagArgsDict', 'WorkspaceCappingArgs', 'WorkspaceCappingArgsDict', 'WorkspaceFeaturesArgs', 'WorkspaceFeaturesArgsDict', 'WorkspaceSkuArgs', 'WorkspaceSkuArgsDict']
class ClusterSkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.float]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, ClusterSkuNameEnum]]]


@pulumi.input_type
class ClusterSkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[Union[_builtins.str, ClusterSkuNameEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, ClusterSkuNameEnum]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterSkuNameEnum]]]): # -> None:
        ...
    


class ColumnArgsDict(TypedDict):
    
    data_type_hint: NotRequired[pulumi.Input[Union[_builtins.str, ColumnDataTypeHintEnum]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ColumnTypeEnum]]]


@pulumi.input_type
class ColumnArgs:
    def __init__(__self__, *, data_type_hint: Optional[pulumi.Input[Union[_builtins.str, ColumnDataTypeHintEnum]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ColumnTypeEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypeHint")
    def data_type_hint(self) -> Optional[pulumi.Input[Union[_builtins.str, ColumnDataTypeHintEnum]]]:
        
        ...
    
    @data_type_hint.setter
    def data_type_hint(self, value: Optional[pulumi.Input[Union[_builtins.str, ColumnDataTypeHintEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ColumnTypeEnum]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ColumnTypeEnum]]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: pulumi.Input[IdentityType]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[IdentityType], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[IdentityType]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[IdentityType]): # -> None:
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
    key_rsa_size: NotRequired[pulumi.Input[_builtins.int]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *, key_name: Optional[pulumi.Input[_builtins.str]] = ..., key_rsa_size: Optional[pulumi.Input[_builtins.int]] = ..., key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ..., key_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRsaSize")
    def key_rsa_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_rsa_size.setter
    def key_rsa_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LogAnalyticsQueryPackQueryPropertiesRelatedArgsDict(TypedDict):
    
    categories: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    solutions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LogAnalyticsQueryPackQueryPropertiesRelatedArgs:
    def __init__(__self__, *, categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., solutions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def solutions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @solutions.setter
    def solutions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MachineReferenceWithHintsArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    kind: pulumi.Input[_builtins.str]


@pulumi.input_type
class MachineReferenceWithHintsArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


class RestoredLogsArgsDict(TypedDict):
    
    end_restore_time: NotRequired[pulumi.Input[_builtins.str]]
    source_table: NotRequired[pulumi.Input[_builtins.str]]
    start_restore_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RestoredLogsArgs:
    def __init__(__self__, *, end_restore_time: Optional[pulumi.Input[_builtins.str]] = ..., source_table: Optional[pulumi.Input[_builtins.str]] = ..., start_restore_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endRestoreTime")
    def end_restore_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_restore_time.setter
    def end_restore_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceTable")
    def source_table(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_table.setter
    def source_table(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startRestoreTime")
    def start_restore_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_restore_time.setter
    def start_restore_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleDefinitionArgsDict(TypedDict):
    
    bin_delay: NotRequired[pulumi.Input[_builtins.int]]
    bin_size: NotRequired[pulumi.Input[_builtins.int]]
    bin_start_time: NotRequired[pulumi.Input[_builtins.str]]
    destination_table: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]
    time_selector: NotRequired[pulumi.Input[Union[_builtins.str, TimeSelectorEnum]]]


@pulumi.input_type
class RuleDefinitionArgs:
    def __init__(__self__, *, bin_delay: Optional[pulumi.Input[_builtins.int]] = ..., bin_size: Optional[pulumi.Input[_builtins.int]] = ..., bin_start_time: Optional[pulumi.Input[_builtins.str]] = ..., destination_table: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ..., time_selector: Optional[pulumi.Input[Union[_builtins.str, TimeSelectorEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binDelay")
    def bin_delay(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bin_delay.setter
    def bin_delay(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binSize")
    def bin_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bin_size.setter
    def bin_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binStartTime")
    def bin_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bin_start_time.setter
    def bin_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_table.setter
    def destination_table(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSelector")
    def time_selector(self) -> Optional[pulumi.Input[Union[_builtins.str, TimeSelectorEnum]]]:
        
        ...
    
    @time_selector.setter
    def time_selector(self, value: Optional[pulumi.Input[Union[_builtins.str, TimeSelectorEnum]]]): # -> None:
        ...
    


class SchemaArgsDict(TypedDict):
    
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[ColumnArgsDict]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *, columns: Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]]:
        
        ...
    
    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SearchResultsArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    end_search_time: NotRequired[pulumi.Input[_builtins.str]]
    limit: NotRequired[pulumi.Input[_builtins.int]]
    query: NotRequired[pulumi.Input[_builtins.str]]
    start_search_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SearchResultsArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., end_search_time: Optional[pulumi.Input[_builtins.str]] = ..., limit: Optional[pulumi.Input[_builtins.int]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ..., start_search_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endSearchTime")
    def end_search_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_search_time.setter
    def end_search_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @limit.setter
    def limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startSearchTime")
    def start_search_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_search_time.setter
    def start_search_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageAccountArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]


@pulumi.input_type
class StorageAccountArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TagArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class TagArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
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
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkspaceCappingArgsDict(TypedDict):
    
    daily_quota_gb: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class WorkspaceCappingArgs:
    def __init__(__self__, *, daily_quota_gb: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyQuotaGb")
    def daily_quota_gb(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @daily_quota_gb.setter
    def daily_quota_gb(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class WorkspaceFeaturesArgsDict(TypedDict):
    
    cluster_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    enable_data_export: NotRequired[pulumi.Input[_builtins.bool]]
    enable_log_access_using_only_resource_permissions: NotRequired[pulumi.Input[_builtins.bool]]
    immediate_purge_data_on30_days: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class WorkspaceFeaturesArgs:
    def __init__(__self__, *, cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_data_export: Optional[pulumi.Input[_builtins.bool]] = ..., enable_log_access_using_only_resource_permissions: Optional[pulumi.Input[_builtins.bool]] = ..., immediate_purge_data_on30_days: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_resource_id.setter
    def cluster_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataExport")
    def enable_data_export(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_data_export.setter
    def enable_data_export(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogAccessUsingOnlyResourcePermissions")
    def enable_log_access_using_only_resource_permissions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_log_access_using_only_resource_permissions.setter
    def enable_log_access_using_only_resource_permissions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @immediate_purge_data_on30_days.setter
    def immediate_purge_data_on30_days(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WorkspaceSkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, WorkspaceSkuNameEnum]]
    capacity_reservation_level: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkspaceSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, WorkspaceSkuNameEnum]], capacity_reservation_level: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, WorkspaceSkuNameEnum]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, WorkspaceSkuNameEnum]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationLevel")
    def capacity_reservation_level(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity_reservation_level.setter
    def capacity_reservation_level(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


