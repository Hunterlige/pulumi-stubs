

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetDeploymentStacksWhatIfResultsAtManagementGroupResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    def properties(self) -> outputs.DeploymentStacksWhatIfResultPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeploymentStacksWhatIfResultsAtManagementGroupResult(GetDeploymentStacksWhatIfResultsAtManagementGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetDeploymentStacksWhatIfResultsAtManagementGroupResult]:
        ...
    


def get_deployment_stacks_what_if_results_at_management_group(deployment_stacks_what_if_result_name: Optional[_builtins.str] = ..., management_group_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeploymentStacksWhatIfResultsAtManagementGroupResult:
    
    ...

def get_deployment_stacks_what_if_results_at_management_group_output(deployment_stacks_what_if_result_name: Optional[pulumi.Input[_builtins.str]] = ..., management_group_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeploymentStacksWhatIfResultsAtManagementGroupResult]:
    
    ...

