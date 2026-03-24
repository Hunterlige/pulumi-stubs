

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
__all__ = ['BrokerArgs', 'Broker']
@pulumi.input_type
class BrokerArgs:
    def __init__(__self__, *, auth_image: pulumi.Input[ContainerImageArgs], broker_image: pulumi.Input[ContainerImageArgs], extended_location: pulumi.Input[ExtendedLocationPropertyArgs], health_manager_image: pulumi.Input[ContainerImageArgs], mode: pulumi.Input[Union[_builtins.str, RunMode]], mq_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], broker_name: Optional[pulumi.Input[_builtins.str]] = ..., broker_node_tolerations: Optional[pulumi.Input[NodeTolerationsArgs]] = ..., cardinality: Optional[pulumi.Input[CardinalityArgs]] = ..., diagnostics: Optional[pulumi.Input[BrokerDiagnosticsArgs]] = ..., disk_backed_message_buffer_settings: Optional[pulumi.Input[DiskBackedMessageBufferSettingsArgs]] = ..., encrypt_internal_traffic: Optional[pulumi.Input[_builtins.bool]] = ..., health_manager_node_tolerations: Optional[pulumi.Input[NodeTolerationsArgs]] = ..., internal_certs: Optional[pulumi.Input[CertManagerCertOptionsArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., memory_profile: Optional[pulumi.Input[Union[_builtins.str, BrokerMemoryProfile]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authImage")
    def auth_image(self) -> pulumi.Input[ContainerImageArgs]:
        
        ...
    
    @auth_image.setter
    def auth_image(self, value: pulumi.Input[ContainerImageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> pulumi.Input[ContainerImageArgs]:
        
        ...
    
    @broker_image.setter
    def broker_image(self, value: pulumi.Input[ContainerImageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationPropertyArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationPropertyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> pulumi.Input[ContainerImageArgs]:
        
        ...
    
    @health_manager_image.setter
    def health_manager_image(self, value: pulumi.Input[ContainerImageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[_builtins.str, RunMode]]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[Union[_builtins.str, RunMode]]): # -> None:
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
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @broker_name.setter
    def broker_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> Optional[pulumi.Input[NodeTolerationsArgs]]:
        
        ...
    
    @broker_node_tolerations.setter
    def broker_node_tolerations(self, value: Optional[pulumi.Input[NodeTolerationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> Optional[pulumi.Input[CardinalityArgs]]:
        
        ...
    
    @cardinality.setter
    def cardinality(self, value: Optional[pulumi.Input[CardinalityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input[BrokerDiagnosticsArgs]]:
        
        ...
    
    @diagnostics.setter
    def diagnostics(self, value: Optional[pulumi.Input[BrokerDiagnosticsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(self) -> Optional[pulumi.Input[DiskBackedMessageBufferSettingsArgs]]:
        
        ...
    
    @disk_backed_message_buffer_settings.setter
    def disk_backed_message_buffer_settings(self, value: Optional[pulumi.Input[DiskBackedMessageBufferSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_internal_traffic.setter
    def encrypt_internal_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(self) -> Optional[pulumi.Input[NodeTolerationsArgs]]:
        
        ...
    
    @health_manager_node_tolerations.setter
    def health_manager_node_tolerations(self, value: Optional[pulumi.Input[NodeTolerationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> Optional[pulumi.Input[CertManagerCertOptionsArgs]]:
        
        ...
    
    @internal_certs.setter
    def internal_certs(self, value: Optional[pulumi.Input[CertManagerCertOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> Optional[pulumi.Input[Union[_builtins.str, BrokerMemoryProfile]]]:
        
        ...
    
    @memory_profile.setter
    def memory_profile(self, value: Optional[pulumi.Input[Union[_builtins.str, BrokerMemoryProfile]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:iotoperationsmq:Broker")
class Broker(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auth_image: Optional[pulumi.Input[Union[ContainerImageArgs, ContainerImageArgsDict]]] = ..., broker_image: Optional[pulumi.Input[Union[ContainerImageArgs, ContainerImageArgsDict]]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., broker_node_tolerations: Optional[pulumi.Input[Union[NodeTolerationsArgs, NodeTolerationsArgsDict]]] = ..., cardinality: Optional[pulumi.Input[Union[CardinalityArgs, CardinalityArgsDict]]] = ..., diagnostics: Optional[pulumi.Input[Union[BrokerDiagnosticsArgs, BrokerDiagnosticsArgsDict]]] = ..., disk_backed_message_buffer_settings: Optional[pulumi.Input[Union[DiskBackedMessageBufferSettingsArgs, DiskBackedMessageBufferSettingsArgsDict]]] = ..., encrypt_internal_traffic: Optional[pulumi.Input[_builtins.bool]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationPropertyArgs, ExtendedLocationPropertyArgsDict]]] = ..., health_manager_image: Optional[pulumi.Input[Union[ContainerImageArgs, ContainerImageArgsDict]]] = ..., health_manager_node_tolerations: Optional[pulumi.Input[Union[NodeTolerationsArgs, NodeTolerationsArgsDict]]] = ..., internal_certs: Optional[pulumi.Input[Union[CertManagerCertOptionsArgs, CertManagerCertOptionsArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., memory_profile: Optional[pulumi.Input[Union[_builtins.str, BrokerMemoryProfile]]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, RunMode]]] = ..., mq_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BrokerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Broker:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authImage")
    def auth_image(self) -> pulumi.Output[outputs.ContainerImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> pulumi.Output[outputs.ContainerImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> pulumi.Output[Optional[outputs.NodeTolerationsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> pulumi.Output[Optional[outputs.CardinalityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> pulumi.Output[Optional[outputs.BrokerDiagnosticsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(self) -> pulumi.Output[Optional[outputs.DiskBackedMessageBufferSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> pulumi.Output[outputs.ContainerImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(self) -> pulumi.Output[Optional[outputs.NodeTolerationsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> pulumi.Output[Optional[outputs.CertManagerCertOptionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]:
        
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
    


