

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeviceArgs', 'Device']
@pulumi.input_type
class DeviceArgs:
    def __init__(__self__, *, global_network_id: pulumi.Input[_builtins.str], aws_location: Optional[pulumi.Input[DeviceAwsLocationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[DeviceLocationArgs]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[pulumi.Input[DeviceAwsLocationArgs]]:
        
        ...
    
    @aws_location.setter
    def aws_location(self, value: Optional[pulumi.Input[DeviceAwsLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[DeviceLocationArgs]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[DeviceLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DeviceState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_location: Optional[pulumi.Input[DeviceAwsLocationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[DeviceLocationArgs]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[pulumi.Input[DeviceAwsLocationArgs]]:
        
        ...
    
    @aws_location.setter
    def aws_location(self, value: Optional[pulumi.Input[DeviceAwsLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[DeviceLocationArgs]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[DeviceLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def vendor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:networkmanager/device:Device")
class Device(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_location: Optional[pulumi.Input[Union[DeviceAwsLocationArgs, DeviceAwsLocationArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Union[DeviceLocationArgs, DeviceLocationArgsDict]]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeviceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_location: Optional[pulumi.Input[Union[DeviceAwsLocationArgs, DeviceAwsLocationArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Union[DeviceLocationArgs, DeviceLocationArgsDict]]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vendor: Optional[pulumi.Input[_builtins.str]] = ...) -> Device:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> pulumi.Output[Optional[outputs.DeviceAwsLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[outputs.DeviceLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


