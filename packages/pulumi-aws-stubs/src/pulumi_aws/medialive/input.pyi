

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InputArgs', 'Input']
@pulumi.input_type
class InputArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], destinations: Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]] = ..., input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]] = ..., input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc: Optional[pulumi.Input[InputVpcArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]]:
        
        ...
    
    @input_devices.setter
    def input_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @input_security_groups.setter
    def input_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]]:
        
        ...
    
    @media_connect_flows.setter
    def media_connect_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]]): # -> None:
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
    def vpc(self) -> Optional[pulumi.Input[InputVpcArgs]]:
        
        ...
    
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[InputVpcArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _InputState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., attached_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]] = ..., input_class: Optional[pulumi.Input[_builtins.str]] = ..., input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]] = ..., input_partner_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_source_type: Optional[pulumi.Input[_builtins.str]] = ..., media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc: Optional[pulumi.Input[InputVpcArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedChannels")
    def attached_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attached_channels.setter
    def attached_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputClass")
    def input_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_class.setter
    def input_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]]:
        
        ...
    
    @input_devices.setter
    def input_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputInputDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputPartnerIds")
    def input_partner_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @input_partner_ids.setter
    def input_partner_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @input_security_groups.setter
    def input_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSourceType")
    def input_source_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_source_type.setter
    def input_source_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]]:
        
        ...
    
    @media_connect_flows.setter
    def media_connect_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputMediaConnectFlowArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input[InputVpcArgs]]:
        
        ...
    
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[InputVpcArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:medialive/input:Input")
class Input(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputDestinationArgs, InputDestinationArgsDict]]]]] = ..., input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputInputDeviceArgs, InputInputDeviceArgsDict]]]]] = ..., input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputMediaConnectFlowArgs, InputMediaConnectFlowArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputSourceArgs, InputSourceArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc: Optional[pulumi.Input[Union[InputVpcArgs, InputVpcArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InputArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., attached_channels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputDestinationArgs, InputDestinationArgsDict]]]]] = ..., input_class: Optional[pulumi.Input[_builtins.str]] = ..., input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputInputDeviceArgs, InputInputDeviceArgsDict]]]]] = ..., input_partner_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_source_type: Optional[pulumi.Input[_builtins.str]] = ..., media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputMediaConnectFlowArgs, InputMediaConnectFlowArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InputSourceArgs, InputSourceArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc: Optional[pulumi.Input[Union[InputVpcArgs, InputVpcArgsDict]]] = ...) -> Input:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedChannels")
    def attached_channels(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence[outputs.InputDestination]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputClass")
    def input_class(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> pulumi.Output[Sequence[outputs.InputInputDevice]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputPartnerIds")
    def input_partner_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSourceType")
    def input_source_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> pulumi.Output[Sequence[outputs.InputMediaConnectFlow]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence[outputs.InputSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> pulumi.Output[Optional[outputs.InputVpc]]:
        
        ...
    


