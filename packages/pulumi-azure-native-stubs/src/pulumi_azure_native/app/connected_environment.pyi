

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectedEnvironmentArgs', 'ConnectedEnvironment']
@pulumi.input_type
class ConnectedEnvironmentArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_configuration: Optional[pulumi.Input[CustomDomainConfigurationArgs]] = ..., dapr_ai_connection_string: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., static_ip: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedEnvironmentName")
    def connected_environment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connected_environment_name.setter
    def connected_environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> Optional[pulumi.Input[CustomDomainConfigurationArgs]]:
        
        ...
    
    @custom_domain_configuration.setter
    def custom_domain_configuration(self, value: Optional[pulumi.Input[CustomDomainConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dapr_ai_connection_string.setter
    def dapr_ai_connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[ExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @static_ip.setter
    def static_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:ConnectedEnvironment")
class ConnectedEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_configuration: Optional[pulumi.Input[Union[CustomDomainConfigurationArgs, CustomDomainConfigurationArgsDict]]] = ..., dapr_ai_connection_string: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., static_ip: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectedEnvironmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConnectedEnvironment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> pulumi.Output[Optional[outputs.CustomDomainConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


