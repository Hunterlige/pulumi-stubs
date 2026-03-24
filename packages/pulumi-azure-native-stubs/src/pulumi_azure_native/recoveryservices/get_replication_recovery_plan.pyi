

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationRecoveryPlanResult', 'AwaitableGetReplicationRecoveryPlanResult', 'get_replication_recovery_plan', 'get_replication_recovery_plan_output']
@pulumi.output_type
class GetReplicationRecoveryPlanResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., type=...) -> None:
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
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.RecoveryPlanPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReplicationRecoveryPlanResult(GetReplicationRecoveryPlanResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationRecoveryPlanResult]:
        ...
    


def get_replication_recovery_plan(recovery_plan_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationRecoveryPlanResult:
    
    ...

def get_replication_recovery_plan_output(recovery_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationRecoveryPlanResult]:
    
    ...

