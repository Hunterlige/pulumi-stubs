

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReachabilityAnalysisIntentResult', 'AwaitableGetReachabilityAnalysisIntentResult', 'get_reachability_analysis_intent', 'get_reachability_analysis_intent_output']
@pulumi.output_type
class GetReachabilityAnalysisIntentResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ReachabilityAnalysisIntentPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReachabilityAnalysisIntentResult(GetReachabilityAnalysisIntentResult):
    def __await__(self): # -> Generator[Never, Any, GetReachabilityAnalysisIntentResult]:
        ...
    


def get_reachability_analysis_intent(network_manager_name: Optional[_builtins.str] = ..., reachability_analysis_intent_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReachabilityAnalysisIntentResult:
    
    ...

def get_reachability_analysis_intent_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., reachability_analysis_intent_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReachabilityAnalysisIntentResult]:
    
    ...

