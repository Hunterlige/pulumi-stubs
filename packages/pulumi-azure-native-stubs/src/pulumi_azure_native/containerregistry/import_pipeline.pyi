

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
__all__ = ['ImportPipelineArgs', 'ImportPipeline']
@pulumi.input_type
class ImportPipelineArgs:
    def __init__(__self__, *, registry_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], source: pulumi.Input[ImportPipelineSourcePropertiesArgs], identity: Optional[pulumi.Input[IdentityPropertiesArgs]] = ..., import_pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PipelineOptions]]]]] = ..., trigger: Optional[pulumi.Input[PipelineTriggerPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def source(self) -> pulumi.Input[ImportPipelineSourcePropertiesArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[ImportPipelineSourcePropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityPropertiesArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importPipelineName")
    def import_pipeline_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_pipeline_name.setter
    def import_pipeline_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PipelineOptions]]]]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PipelineOptions]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[PipelineTriggerPropertiesArgs]]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[PipelineTriggerPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:containerregistry:ImportPipeline")
class ImportPipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., identity: Optional[pulumi.Input[Union[IdentityPropertiesArgs, IdentityPropertiesArgsDict]]] = ..., import_pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PipelineOptions]]]]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[ImportPipelineSourcePropertiesArgs, ImportPipelineSourcePropertiesArgsDict]]] = ..., trigger: Optional[pulumi.Input[Union[PipelineTriggerPropertiesArgs, PipelineTriggerPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ImportPipelineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ImportPipeline:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.ImportPipelineSourcePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> pulumi.Output[Optional[outputs.PipelineTriggerPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


