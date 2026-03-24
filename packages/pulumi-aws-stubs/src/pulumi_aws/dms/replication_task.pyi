

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ReplicationTaskArgs', 'ReplicationTask']
@pulumi.input_type
class ReplicationTaskArgs:
    def __init__(__self__, *, migration_type: pulumi.Input[_builtins.str], replication_instance_arn: pulumi.Input[_builtins.str], replication_task_id: pulumi.Input[_builtins.str], source_endpoint_arn: pulumi.Input[_builtins.str], table_mappings: pulumi.Input[_builtins.str], target_endpoint_arn: pulumi.Input[_builtins.str], cdc_start_position: Optional[pulumi.Input[_builtins.str]] = ..., cdc_start_time: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_settings: Optional[pulumi.Input[_builtins.str]] = ..., resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., start_replication_task: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationType")
    def migration_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @migration_type.setter
    def migration_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replication_instance_arn.setter
    def replication_instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskId")
    def replication_task_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replication_task_id.setter
    def replication_task_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_mappings.setter
    def table_mappings(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartPosition")
    def cdc_start_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cdc_start_position.setter
    def cdc_start_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartTime")
    def cdc_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cdc_start_time.setter
    def cdc_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskSettings")
    def replication_task_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_task_settings.setter
    def replication_task_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startReplicationTask")
    def start_replication_task(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_replication_task.setter
    def start_replication_task(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ReplicationTaskState:
    def __init__(__self__, *, cdc_start_position: Optional[pulumi.Input[_builtins.str]] = ..., cdc_start_time: Optional[pulumi.Input[_builtins.str]] = ..., migration_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_settings: Optional[pulumi.Input[_builtins.str]] = ..., resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ..., start_replication_task: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., table_mappings: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartPosition")
    def cdc_start_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cdc_start_position.setter
    def cdc_start_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartTime")
    def cdc_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cdc_start_time.setter
    def cdc_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationType")
    def migration_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_type.setter
    def migration_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_instance_arn.setter
    def replication_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskArn")
    def replication_task_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_task_arn.setter
    def replication_task_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskId")
    def replication_task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_task_id.setter
    def replication_task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskSettings")
    def replication_task_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_task_settings.setter
    def replication_task_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startReplicationTask")
    def start_replication_task(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_replication_task.setter
    def start_replication_task(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_mappings.setter
    def table_mappings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:dms/replicationTask:ReplicationTask")
class ReplicationTask(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cdc_start_position: Optional[pulumi.Input[_builtins.str]] = ..., cdc_start_time: Optional[pulumi.Input[_builtins.str]] = ..., migration_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_settings: Optional[pulumi.Input[_builtins.str]] = ..., resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ..., start_replication_task: Optional[pulumi.Input[_builtins.bool]] = ..., table_mappings: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ReplicationTaskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cdc_start_position: Optional[pulumi.Input[_builtins.str]] = ..., cdc_start_time: Optional[pulumi.Input[_builtins.str]] = ..., migration_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_task_settings: Optional[pulumi.Input[_builtins.str]] = ..., resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ..., start_replication_task: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., table_mappings: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> ReplicationTask:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartPosition")
    def cdc_start_position(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartTime")
    def cdc_start_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationType")
    def migration_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskArn")
    def replication_task_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskId")
    def replication_task_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskSettings")
    def replication_task_settings(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startReplicationTask")
    def start_replication_task(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


