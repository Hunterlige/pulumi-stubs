

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProfileAgentArgs', 'ProfileAgent']
@pulumi.input_type
class ProfileAgentArgs:
    def __init__(__self__, *, custom_domains: pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]], profile_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], web_agent: pulumi.Input[ResourceReferenceArgs], agent_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]:
        
        ...
    
    @custom_domains.setter
    def custom_domains(self, value: pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAgent")
    def web_agent(self) -> pulumi.Input[ResourceReferenceArgs]:
        
        ...
    
    @web_agent.setter
    def web_agent(self, value: pulumi.Input[ResourceReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cdn:ProfileAgent")
class ProfileAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]]]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., web_agent: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProfileAgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ProfileAgent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Sequence[outputs.ResourceReferenceResponse]]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAgent")
    def web_agent(self) -> pulumi.Output[outputs.ResourceReferenceResponse]:
        
        ...
    


