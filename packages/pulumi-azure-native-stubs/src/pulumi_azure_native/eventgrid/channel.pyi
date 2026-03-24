

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
__all__ = ['ChannelArgs', 'Channel']
@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *, partner_namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], channel_name: Optional[pulumi.Input[_builtins.str]] = ..., channel_type: Optional[pulumi.Input[Union[_builtins.str, ChannelType]]] = ..., expiration_time_if_not_activated_utc: Optional[pulumi.Input[_builtins.str]] = ..., message_for_activation: Optional[pulumi.Input[_builtins.str]] = ..., partner_topic_info: Optional[pulumi.Input[PartnerTopicInfoArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ChannelProvisioningState]]] = ..., readiness_state: Optional[pulumi.Input[Union[_builtins.str, ReadinessState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerNamespaceName")
    def partner_namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @partner_namespace_name.setter
    def partner_namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ChannelType]]]:
        
        ...
    
    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ChannelType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time_if_not_activated_utc.setter
    def expiration_time_if_not_activated_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_for_activation.setter
    def message_for_activation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerTopicInfo")
    def partner_topic_info(self) -> Optional[pulumi.Input[PartnerTopicInfoArgs]]:
        
        ...
    
    @partner_topic_info.setter
    def partner_topic_info(self, value: Optional[pulumi.Input[PartnerTopicInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ChannelProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ChannelProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessState")
    def readiness_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ReadinessState]]]:
        
        ...
    
    @readiness_state.setter
    def readiness_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ReadinessState]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventgrid:Channel")
class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., channel_type: Optional[pulumi.Input[Union[_builtins.str, ChannelType]]] = ..., expiration_time_if_not_activated_utc: Optional[pulumi.Input[_builtins.str]] = ..., message_for_activation: Optional[pulumi.Input[_builtins.str]] = ..., partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_topic_info: Optional[pulumi.Input[Union[PartnerTopicInfoArgs, PartnerTopicInfoArgsDict]]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ChannelProvisioningState]]] = ..., readiness_state: Optional[pulumi.Input[Union[_builtins.str, ReadinessState]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChannelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Channel:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerTopicInfo")
    def partner_topic_info(self) -> pulumi.Output[Optional[outputs.PartnerTopicInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessState")
    def readiness_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


