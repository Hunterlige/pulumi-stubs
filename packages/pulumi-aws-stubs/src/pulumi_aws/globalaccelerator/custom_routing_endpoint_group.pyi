

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
__all__ = ['CustomRoutingEndpointGroupArgs', 'CustomRoutingEndpointGroup']
@pulumi.input_type
class CustomRoutingEndpointGroupArgs:
    def __init__(__self__, *, destination_configurations: pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]], listener_arn: pulumi.Input[_builtins.str], endpoint_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]] = ..., endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigurations")
    def destination_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]]:
        
        ...
    
    @destination_configurations.setter
    def destination_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @listener_arn.setter
    def listener_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]]:
        
        ...
    
    @endpoint_configurations.setter
    def endpoint_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_group_region.setter
    def endpoint_group_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CustomRoutingEndpointGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]]] = ..., endpoint_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]] = ..., endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigurations")
    def destination_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]]]:
        
        ...
    
    @destination_configurations.setter
    def destination_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupDestinationConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]]:
        
        ...
    
    @endpoint_configurations.setter
    def endpoint_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRoutingEndpointGroupEndpointConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_group_region.setter
    def endpoint_group_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @listener_arn.setter
    def listener_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CustomRoutingEndpointGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomRoutingEndpointGroupDestinationConfigurationArgs, CustomRoutingEndpointGroupDestinationConfigurationArgsDict]]]]] = ..., endpoint_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomRoutingEndpointGroupEndpointConfigurationArgs, CustomRoutingEndpointGroupEndpointConfigurationArgsDict]]]]] = ..., endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomRoutingEndpointGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomRoutingEndpointGroupDestinationConfigurationArgs, CustomRoutingEndpointGroupDestinationConfigurationArgsDict]]]]] = ..., endpoint_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomRoutingEndpointGroupEndpointConfigurationArgs, CustomRoutingEndpointGroupEndpointConfigurationArgsDict]]]]] = ..., endpoint_group_region: Optional[pulumi.Input[_builtins.str]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomRoutingEndpointGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigurations")
    def destination_configurations(self) -> pulumi.Output[Sequence[outputs.CustomRoutingEndpointGroupDestinationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.CustomRoutingEndpointGroupEndpointConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointGroupRegion")
    def endpoint_group_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


