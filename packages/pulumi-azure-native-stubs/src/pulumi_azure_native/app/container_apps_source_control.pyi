

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContainerAppsSourceControlArgs', 'ContainerAppsSourceControl']
@pulumi.input_type
class ContainerAppsSourceControlArgs:
    def __init__(__self__, *, container_app_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], branch: Optional[pulumi.Input[_builtins.str]] = ..., github_action_configuration: Optional[pulumi.Input[GithubActionConfigurationArgs]] = ..., repo_url: Optional[pulumi.Input[_builtins.str]] = ..., source_control_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAppName")
    def container_app_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_app_name.setter
    def container_app_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> Optional[pulumi.Input[GithubActionConfigurationArgs]]:
        
        ...
    
    @github_action_configuration.setter
    def github_action_configuration(self, value: Optional[pulumi.Input[GithubActionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repo_url.setter
    def repo_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceControlName")
    def source_control_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_control_name.setter
    def source_control_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:ContainerAppsSourceControl")
class ContainerAppsSourceControl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., branch: Optional[pulumi.Input[_builtins.str]] = ..., container_app_name: Optional[pulumi.Input[_builtins.str]] = ..., github_action_configuration: Optional[pulumi.Input[Union[GithubActionConfigurationArgs, GithubActionConfigurationArgsDict]]] = ..., repo_url: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_control_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContainerAppsSourceControlArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ContainerAppsSourceControl:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> pulumi.Output[Optional[outputs.GithubActionConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationState")
    def operation_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


