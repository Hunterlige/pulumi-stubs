

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseArgs', 'Database']
@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *, location_id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], app_engine_integration_mode: Optional[pulumi.Input[_builtins.str]] = ..., cmek_config: Optional[pulumi.Input[DatabaseCmekConfigArgs]] = ..., concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., database_edition: Optional[pulumi.Input[_builtins.str]] = ..., delete_protection_state: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., firestore_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., mongodb_compatible_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery_enablement: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_updates_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location_id.setter
    def location_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineIntegrationMode")
    def app_engine_integration_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_engine_integration_mode.setter
    def app_engine_integration_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfig")
    def cmek_config(self) -> Optional[pulumi.Input[DatabaseCmekConfigArgs]]:
        
        ...
    
    @cmek_config.setter
    def cmek_config(self, value: Optional[pulumi.Input[DatabaseCmekConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @concurrency_mode.setter
    def concurrency_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_edition.setter
    def database_edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtectionState")
    def delete_protection_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_protection_state.setter
    def delete_protection_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firestoreDataAccessMode")
    def firestore_data_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firestore_data_access_mode.setter
    def firestore_data_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbCompatibleDataAccessMode")
    def mongodb_compatible_data_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mongodb_compatible_data_access_mode.setter
    def mongodb_compatible_data_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnablement")
    def point_in_time_recovery_enablement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @point_in_time_recovery_enablement.setter
    def point_in_time_recovery_enablement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeUpdatesMode")
    def realtime_updates_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_updates_mode.setter
    def realtime_updates_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *, app_engine_integration_mode: Optional[pulumi.Input[_builtins.str]] = ..., cmek_config: Optional[pulumi.Input[DatabaseCmekConfigArgs]] = ..., concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_edition: Optional[pulumi.Input[_builtins.str]] = ..., delete_protection_state: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., earliest_version_time: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., firestore_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., mongodb_compatible_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery_enablement: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_updates_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version_retention_period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineIntegrationMode")
    def app_engine_integration_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_engine_integration_mode.setter
    def app_engine_integration_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfig")
    def cmek_config(self) -> Optional[pulumi.Input[DatabaseCmekConfigArgs]]:
        
        ...
    
    @cmek_config.setter
    def cmek_config(self, value: Optional[pulumi.Input[DatabaseCmekConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @concurrency_mode.setter
    def concurrency_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_edition.setter
    def database_edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtectionState")
    def delete_protection_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_protection_state.setter
    def delete_protection_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestVersionTime")
    def earliest_version_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @earliest_version_time.setter
    def earliest_version_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firestoreDataAccessMode")
    def firestore_data_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firestore_data_access_mode.setter
    def firestore_data_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_id.setter
    def location_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbCompatibleDataAccessMode")
    def mongodb_compatible_data_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mongodb_compatible_data_access_mode.setter
    def mongodb_compatible_data_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnablement")
    def point_in_time_recovery_enablement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @point_in_time_recovery_enablement.setter
    def point_in_time_recovery_enablement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeUpdatesMode")
    def realtime_updates_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_updates_mode.setter
    def realtime_updates_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionRetentionPeriod")
    def version_retention_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_retention_period.setter
    def version_retention_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firestore/database:Database")
class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_engine_integration_mode: Optional[pulumi.Input[_builtins.str]] = ..., cmek_config: Optional[pulumi.Input[Union[DatabaseCmekConfigArgs, DatabaseCmekConfigArgsDict]]] = ..., concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., database_edition: Optional[pulumi.Input[_builtins.str]] = ..., delete_protection_state: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., firestore_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., mongodb_compatible_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery_enablement: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_updates_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_engine_integration_mode: Optional[pulumi.Input[_builtins.str]] = ..., cmek_config: Optional[pulumi.Input[Union[DatabaseCmekConfigArgs, DatabaseCmekConfigArgsDict]]] = ..., concurrency_mode: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_edition: Optional[pulumi.Input[_builtins.str]] = ..., delete_protection_state: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., earliest_version_time: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., firestore_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix: Optional[pulumi.Input[_builtins.str]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., mongodb_compatible_data_access_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery_enablement: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_updates_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version_retention_period: Optional[pulumi.Input[_builtins.str]] = ...) -> Database:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineIntegrationMode")
    def app_engine_integration_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfig")
    def cmek_config(self) -> pulumi.Output[Optional[outputs.DatabaseCmekConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrencyMode")
    def concurrency_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtectionState")
    def delete_protection_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestVersionTime")
    def earliest_version_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firestoreDataAccessMode")
    def firestore_data_access_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mongodbCompatibleDataAccessMode")
    def mongodb_compatible_data_access_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnablement")
    def point_in_time_recovery_enablement(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeUpdatesMode")
    def realtime_updates_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionRetentionPeriod")
    def version_retention_period(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


