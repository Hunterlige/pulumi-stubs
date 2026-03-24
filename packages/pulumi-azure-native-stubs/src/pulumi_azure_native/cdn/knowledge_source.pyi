

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KnowledgeSourceArgs', 'KnowledgeSource']
@pulumi.input_type
class KnowledgeSourceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], source_type: pulumi.Input[Union[_builtins.str, KnowledgeSourceType]], url: pulumi.Input[_builtins.str], web_agent_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_source_name: Optional[pulumi.Input[_builtins.str]] = ..., update_frequency: Optional[pulumi.Input[Union[_builtins.str, KnowledgeSourceUpdateFrequency]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[Union[_builtins.str, KnowledgeSourceType]]:
        
        ...
    
    @source_type.setter
    def source_type(self, value: pulumi.Input[Union[_builtins.str, KnowledgeSourceType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAgentName")
    def web_agent_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @web_agent_name.setter
    def web_agent_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeSourceName")
    def knowledge_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @knowledge_source_name.setter
    def knowledge_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateFrequency")
    def update_frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, KnowledgeSourceUpdateFrequency]]]:
        
        ...
    
    @update_frequency.setter
    def update_frequency(self, value: Optional[pulumi.Input[Union[_builtins.str, KnowledgeSourceUpdateFrequency]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cdn:KnowledgeSource")
class KnowledgeSource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_source_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_type: Optional[pulumi.Input[Union[_builtins.str, KnowledgeSourceType]]] = ..., update_frequency: Optional[pulumi.Input[Union[_builtins.str, KnowledgeSourceUpdateFrequency]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., web_agent_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: KnowledgeSourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> KnowledgeSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshedTime")
    def last_refreshed_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="updateFrequency")
    def update_frequency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


