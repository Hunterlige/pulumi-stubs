

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BrokerAuthorizationArgs', 'BrokerAuthorization']
@pulumi.input_type
class BrokerAuthorizationArgs:
    def __init__(__self__, *, authorization_policies: pulumi.Input[AuthorizationConfigArgs], broker_name: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationPropertyArgs], listener_ref: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], mq_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], authorization_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(self) -> pulumi.Input[AuthorizationConfigArgs]:
        
        ...
    
    @authorization_policies.setter
    def authorization_policies(self, value: pulumi.Input[AuthorizationConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @broker_name.setter
    def broker_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationPropertyArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationPropertyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerRef")
    def listener_ref(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @listener_ref.setter
    def listener_ref(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mq_name.setter
    def mq_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationName")
    def authorization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_name.setter
    def authorization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotoperationsmq:BrokerAuthorization")
class BrokerAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization_name: Optional[pulumi.Input[_builtins.str]] = ..., authorization_policies: Optional[pulumi.Input[Union[AuthorizationConfigArgs, AuthorizationConfigArgsDict]]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationPropertyArgs, ExtendedLocationPropertyArgsDict]]] = ..., listener_ref: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mq_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BrokerAuthorizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BrokerAuthorization:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(self) -> pulumi.Output[outputs.AuthorizationConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerRef")
    def listener_ref(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    


