

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseAdvisorResult', 'AwaitableGetDatabaseAdvisorResult', 'get_database_advisor', 'get_database_advisor_output']
@pulumi.output_type
class GetDatabaseAdvisorResult:
    
    def __init__(__self__, advisor_status=..., auto_execute_status=..., auto_execute_status_inherited_from=..., azure_api_version=..., id=..., kind=..., last_checked=..., location=..., name=..., recommendations_status=..., recommended_actions=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advisorStatus")
    def advisor_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoExecuteStatus")
    def auto_execute_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoExecuteStatusInheritedFrom")
    def auto_execute_status_inherited_from(self) -> _builtins.str:
        
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
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationsStatus")
    def recommendations_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedActions")
    def recommended_actions(self) -> Sequence[outputs.RecommendedActionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDatabaseAdvisorResult(GetDatabaseAdvisorResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseAdvisorResult]:
        ...
    


def get_database_advisor(advisor_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseAdvisorResult:
    
    ...

def get_database_advisor_output(advisor_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseAdvisorResult]:
    
    ...

