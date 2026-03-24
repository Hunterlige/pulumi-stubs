

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SourceControlArgs', 'SourceControl']
@pulumi.input_type
class SourceControlArgs:
    def __init__(__self__, *, content_types: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ContentType]]]], display_name: pulumi.Input[_builtins.str], repo_type: pulumi.Input[Union[_builtins.str, RepoType]], repository: pulumi.Input[RepositoryArgs], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., last_deployment_info: Optional[pulumi.Input[DeploymentInfoArgs]] = ..., repository_resource_info: Optional[pulumi.Input[RepositoryResourceInfoArgs]] = ..., source_control_id: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, Version]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ContentType]]]]:
        
        ...
    
    @content_types.setter
    def content_types(self, value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ContentType]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Input[Union[_builtins.str, RepoType]]:
        
        ...
    
    @repo_type.setter
    def repo_type(self, value: pulumi.Input[Union[_builtins.str, RepoType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[RepositoryArgs]:
        
        ...
    
    @repository.setter
    def repository(self, value: pulumi.Input[RepositoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDeploymentInfo")
    def last_deployment_info(self) -> Optional[pulumi.Input[DeploymentInfoArgs]]:
        
        ...
    
    @last_deployment_info.setter
    def last_deployment_info(self, value: Optional[pulumi.Input[DeploymentInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryResourceInfo")
    def repository_resource_info(self) -> Optional[pulumi.Input[RepositoryResourceInfoArgs]]:
        
        ...
    
    @repository_resource_info.setter
    def repository_resource_info(self, value: Optional[pulumi.Input[RepositoryResourceInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceControlId")
    def source_control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_control_id.setter
    def source_control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, Version]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, Version]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:SourceControl")
class SourceControl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., content_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ContentType]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., last_deployment_info: Optional[pulumi.Input[Union[DeploymentInfoArgs, DeploymentInfoArgsDict]]] = ..., repo_type: Optional[pulumi.Input[Union[_builtins.str, RepoType]]] = ..., repository: Optional[pulumi.Input[Union[RepositoryArgs, RepositoryArgsDict]]] = ..., repository_resource_info: Optional[pulumi.Input[Union[RepositoryResourceInfoArgs, RepositoryResourceInfoArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_control_id: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, Version]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SourceControlArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SourceControl:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDeploymentInfo")
    def last_deployment_info(self) -> pulumi.Output[Optional[outputs.DeploymentInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[outputs.RepositoryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryResourceInfo")
    def repository_resource_info(self) -> pulumi.Output[Optional[outputs.RepositoryResourceInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


