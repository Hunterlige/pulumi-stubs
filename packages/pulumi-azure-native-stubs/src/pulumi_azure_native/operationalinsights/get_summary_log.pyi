

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSummaryLogResult', 'AwaitableGetSummaryLogResult', 'get_summary_log', 'get_summary_log_output']
@pulumi.output_type
class GetSummaryLogResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., is_active=..., name=..., provisioning_state=..., rule_definition=..., rule_type=..., status_code=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(self) -> Optional[outputs.RuleDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSummaryLogResult(GetSummaryLogResult):
    def __await__(self): # -> Generator[Never, Any, GetSummaryLogResult]:
        ...
    


def get_summary_log(resource_group_name: Optional[_builtins.str] = ..., summary_logs_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSummaryLogResult:
    
    ...

def get_summary_log_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., summary_logs_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSummaryLogResult]:
    
    ...

