

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContainerAppsSourceControlResult', 'AwaitableGetContainerAppsSourceControlResult', 'get_container_apps_source_control', 'get_container_apps_source_control_output']
@pulumi.output_type
class GetContainerAppsSourceControlResult:
    
    def __init__(__self__, azure_api_version=..., branch=..., github_action_configuration=..., id=..., name=..., operation_state=..., repo_url=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> Optional[outputs.GithubActionConfigurationResponse]:
        
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
    @pulumi.getter(name="operationState")
    def operation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetContainerAppsSourceControlResult(GetContainerAppsSourceControlResult):
    def __await__(self): # -> Generator[Never, Any, GetContainerAppsSourceControlResult]:
        ...
    


def get_container_apps_source_control(container_app_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., source_control_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContainerAppsSourceControlResult:
    
    ...

def get_container_apps_source_control_output(container_app_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_control_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContainerAppsSourceControlResult]:
    
    ...

