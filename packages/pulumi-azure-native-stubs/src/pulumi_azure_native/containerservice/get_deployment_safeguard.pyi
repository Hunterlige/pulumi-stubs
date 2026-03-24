

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDeploymentSafeguardResult', 'AwaitableGetDeploymentSafeguardResult', 'get_deployment_safeguard', 'get_deployment_safeguard_output']
@pulumi.output_type
class GetDeploymentSafeguardResult:
    
    def __init__(__self__, azure_api_version=..., e_tag=..., excluded_namespaces=..., id=..., level=..., name=..., provisioning_state=..., system_data=..., system_excluded_namespaces=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedNamespaces")
    def excluded_namespaces(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemExcludedNamespaces")
    def system_excluded_namespaces(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeploymentSafeguardResult(GetDeploymentSafeguardResult):
    def __await__(self): # -> Generator[Never, Any, GetDeploymentSafeguardResult]:
        ...
    


def get_deployment_safeguard(resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeploymentSafeguardResult:
    
    ...

def get_deployment_safeguard_output(resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeploymentSafeguardResult]:
    
    ...

