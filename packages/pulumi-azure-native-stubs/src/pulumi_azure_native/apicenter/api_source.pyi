

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiSourceArgs', 'ApiSource']
@pulumi.input_type
class ApiSourceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], api_source_name: Optional[pulumi.Input[_builtins.str]] = ..., azure_api_management_source: Optional[pulumi.Input[AzureApiManagementSourceArgs]] = ..., import_specification: Optional[pulumi.Input[Union[_builtins.str, ImportSpecificationOptions]]] = ..., target_environment_id: Optional[pulumi.Input[_builtins.str]] = ..., target_lifecycle_stage: Optional[pulumi.Input[Union[_builtins.str, LifecycleStage]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSourceName")
    def api_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_source_name.setter
    def api_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiManagementSource")
    def azure_api_management_source(self) -> Optional[pulumi.Input[AzureApiManagementSourceArgs]]:
        
        ...
    
    @azure_api_management_source.setter
    def azure_api_management_source(self, value: Optional[pulumi.Input[AzureApiManagementSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSpecification")
    def import_specification(self) -> Optional[pulumi.Input[Union[_builtins.str, ImportSpecificationOptions]]]:
        
        ...
    
    @import_specification.setter
    def import_specification(self, value: Optional[pulumi.Input[Union[_builtins.str, ImportSpecificationOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEnvironmentId")
    def target_environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_environment_id.setter
    def target_environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLifecycleStage")
    def target_lifecycle_stage(self) -> Optional[pulumi.Input[Union[_builtins.str, LifecycleStage]]]:
        
        ...
    
    @target_lifecycle_stage.setter
    def target_lifecycle_stage(self, value: Optional[pulumi.Input[Union[_builtins.str, LifecycleStage]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apicenter:ApiSource")
class ApiSource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_source_name: Optional[pulumi.Input[_builtins.str]] = ..., azure_api_management_source: Optional[pulumi.Input[Union[AzureApiManagementSourceArgs, AzureApiManagementSourceArgsDict]]] = ..., import_specification: Optional[pulumi.Input[Union[_builtins.str, ImportSpecificationOptions]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., target_environment_id: Optional[pulumi.Input[_builtins.str]] = ..., target_lifecycle_stage: Optional[pulumi.Input[Union[_builtins.str, LifecycleStage]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApiSourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ApiSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiManagementSource")
    def azure_api_management_source(self) -> pulumi.Output[Optional[outputs.AzureApiManagementSourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSpecification")
    def import_specification(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkState")
    def link_state(self) -> pulumi.Output[outputs.LinkStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEnvironmentId")
    def target_environment_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLifecycleStage")
    def target_lifecycle_stage(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


