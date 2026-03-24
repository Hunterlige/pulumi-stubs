

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkloadDeploymentSecretConfigurationsResult', ..., 'get_workload_deployment_secret_configurations', ...]
@pulumi.output_type
class GetWorkloadDeploymentSecretConfigurationsResult:
    
    def __init__(__self__, id=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    def properties(self) -> outputs.WorkloadDeploymentModelPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.WorkloadDeploymentModelResponseSystemData:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkloadDeploymentSecretConfigurationsResult(GetWorkloadDeploymentSecretConfigurationsResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkloadDeploymentSecretConfigurationsResult]:
        ...
    


def get_workload_deployment_secret_configurations(modernize_project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., workload_deployment_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkloadDeploymentSecretConfigurationsResult:
    
    ...

def get_workload_deployment_secret_configurations_output(modernize_project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workload_deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkloadDeploymentSecretConfigurationsResult]:
    
    ...

