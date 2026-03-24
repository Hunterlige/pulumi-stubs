

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationLinkResult', 'AwaitableGetReplicationLinkResult', 'get_replication_link', 'get_replication_link_output']
@pulumi.output_type
class GetReplicationLinkResult:
    
    def __init__(__self__, azure_api_version=..., id=..., is_termination_allowed=..., link_type=..., name=..., partner_database=..., partner_database_id=..., partner_location=..., partner_role=..., partner_server=..., percent_complete=..., replication_mode=..., replication_state=..., role=..., start_time=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTerminationAllowed")
    def is_termination_allowed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerDatabase")
    def partner_database(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerDatabaseId")
    def partner_database_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerLocation")
    def partner_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerRole")
    def partner_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerServer")
    def partner_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReplicationLinkResult(GetReplicationLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationLinkResult]:
        ...
    


def get_replication_link(database_name: Optional[_builtins.str] = ..., link_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationLinkResult:
    
    ...

def get_replication_link_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationLinkResult]:
    
    ...

