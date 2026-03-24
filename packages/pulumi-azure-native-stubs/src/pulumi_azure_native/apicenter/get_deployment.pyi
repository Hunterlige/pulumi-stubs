

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDeploymentResult', 'AwaitableGetDeploymentResult', 'get_deployment', 'get_deployment_output']
@pulumi.output_type
class GetDeploymentResult:
    
    def __init__(__self__, azure_api_version=..., custom_properties=..., definition_id=..., description=..., environment_id=..., id=..., name=..., server=..., state=..., system_data=..., title=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionId")
    def definition_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]:
        
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
    def server(self) -> Optional[outputs.DeploymentServerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeploymentResult(GetDeploymentResult):
    def __await__(self): # -> Generator[Never, Any, GetDeploymentResult]:
        ...
    


def get_deployment(api_name: Optional[_builtins.str] = ..., deployment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeploymentResult:
    
    ...

def get_deployment_output(api_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeploymentResult]:
    
    ...

