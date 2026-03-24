

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationTaskResult', 'AwaitableGetReplicationTaskResult', 'get_replication_task', 'get_replication_task_output']
@pulumi.output_type
class GetReplicationTaskResult:
    
    def __init__(__self__, cdc_start_position=..., cdc_start_time=..., id=..., migration_type=..., region=..., replication_instance_arn=..., replication_task_arn=..., replication_task_id=..., replication_task_settings=..., source_endpoint_arn=..., start_replication_task=..., status=..., table_mappings=..., tags=..., target_endpoint_arn=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartPosition")
    def cdc_start_position(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcStartTime")
    def cdc_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationType")
    def migration_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskArn")
    def replication_task_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskId")
    def replication_task_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTaskSettings")
    def replication_task_settings(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startReplicationTask")
    def start_replication_task(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReplicationTaskResult(GetReplicationTaskResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationTaskResult]:
        ...
    


def get_replication_task(region: Optional[_builtins.str] = ..., replication_task_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationTaskResult:
    
    ...

def get_replication_task_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., replication_task_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationTaskResult]:
    
    ...

