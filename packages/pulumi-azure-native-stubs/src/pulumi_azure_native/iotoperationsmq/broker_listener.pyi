

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
__all__ = ['BrokerListenerArgs', 'BrokerListener']
@pulumi.input_type
class BrokerListenerArgs:
    def __init__(__self__, *, broker_name: pulumi.Input[_builtins.str], broker_ref: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationPropertyArgs], mq_name: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int], resource_group_name: pulumi.Input[_builtins.str], authentication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., listener_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., node_port: Optional[pulumi.Input[_builtins.int]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_type: Optional[pulumi.Input[Union[_builtins.str, ServiceType]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls: Optional[pulumi.Input[TlsCertMethodArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @broker_name.setter
    def broker_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerRef")
    def broker_ref(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @broker_ref.setter
    def broker_ref(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationPropertyArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationPropertyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mq_name.setter
    def mq_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationEnabled")
    def authentication_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @authentication_enabled.setter
    def authentication_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEnabled")
    def authorization_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @authorization_enabled.setter
    def authorization_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerName")
    def listener_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @listener_name.setter
    def listener_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePort")
    def node_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_port.setter
    def node_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceType]]]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[TlsCertMethodArgs]]:
        
        ...
    
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[TlsCertMethodArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotoperationsmq:BrokerListener")
class BrokerListener(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authentication_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., broker_ref: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationPropertyArgs, ExtendedLocationPropertyArgsDict]]] = ..., listener_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mq_name: Optional[pulumi.Input[_builtins.str]] = ..., node_port: Optional[pulumi.Input[_builtins.int]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_type: Optional[pulumi.Input[Union[_builtins.str, ServiceType]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls: Optional[pulumi.Input[Union[TlsCertMethodArgs, TlsCertMethodArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BrokerListenerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BrokerListener:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationEnabled")
    def authentication_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEnabled")
    def authorization_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerRef")
    def broker_ref(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationPropertyResponse]:
        
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
    @pulumi.getter(name="nodePort")
    def node_port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def tls(self) -> pulumi.Output[Optional[outputs.TlsCertMethodResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


