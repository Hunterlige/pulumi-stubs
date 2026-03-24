

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
__all__ = ['EventDestinationArgs', 'EventDestination']
@pulumi.input_type
class EventDestinationArgs:
    def __init__(__self__, *, configuration_set_name: pulumi.Input[_builtins.str], matching_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kinesis_destination: Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_destination: Optional[pulumi.Input[EventDestinationSnsDestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingTypes")
    def matching_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @matching_types.setter
    def matching_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchDestinations")
    def cloudwatch_destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]]:
        
        ...
    
    @cloudwatch_destinations.setter
    def cloudwatch_destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDestination")
    def kinesis_destination(self) -> Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]]:
        
        ...
    
    @kinesis_destination.setter
    def kinesis_destination(self, value: Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]]): # -> None:
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
    @pulumi.getter(name="snsDestination")
    def sns_destination(self) -> Optional[pulumi.Input[EventDestinationSnsDestinationArgs]]:
        
        ...
    
    @sns_destination.setter
    def sns_destination(self, value: Optional[pulumi.Input[EventDestinationSnsDestinationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _EventDestinationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kinesis_destination: Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]] = ..., matching_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_destination: Optional[pulumi.Input[EventDestinationSnsDestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchDestinations")
    def cloudwatch_destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]]:
        
        ...
    
    @cloudwatch_destinations.setter
    def cloudwatch_destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventDestinationCloudwatchDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDestination")
    def kinesis_destination(self) -> Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]]:
        
        ...
    
    @kinesis_destination.setter
    def kinesis_destination(self, value: Optional[pulumi.Input[EventDestinationKinesisDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingTypes")
    def matching_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @matching_types.setter
    def matching_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="snsDestination")
    def sns_destination(self) -> Optional[pulumi.Input[EventDestinationSnsDestinationArgs]]:
        
        ...
    
    @sns_destination.setter
    def sns_destination(self, value: Optional[pulumi.Input[EventDestinationSnsDestinationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:ses/eventDestination:EventDestination")
class EventDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventDestinationCloudwatchDestinationArgs, EventDestinationCloudwatchDestinationArgsDict]]]]] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kinesis_destination: Optional[pulumi.Input[Union[EventDestinationKinesisDestinationArgs, EventDestinationKinesisDestinationArgsDict]]] = ..., matching_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_destination: Optional[pulumi.Input[Union[EventDestinationSnsDestinationArgs, EventDestinationSnsDestinationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventDestinationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventDestinationCloudwatchDestinationArgs, EventDestinationCloudwatchDestinationArgsDict]]]]] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kinesis_destination: Optional[pulumi.Input[Union[EventDestinationKinesisDestinationArgs, EventDestinationKinesisDestinationArgsDict]]] = ..., matching_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_destination: Optional[pulumi.Input[Union[EventDestinationSnsDestinationArgs, EventDestinationSnsDestinationArgsDict]]] = ...) -> EventDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchDestinations")
    def cloudwatch_destinations(self) -> pulumi.Output[Optional[Sequence[outputs.EventDestinationCloudwatchDestination]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDestination")
    def kinesis_destination(self) -> pulumi.Output[Optional[outputs.EventDestinationKinesisDestination]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingTypes")
    def matching_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="snsDestination")
    def sns_destination(self) -> pulumi.Output[Optional[outputs.EventDestinationSnsDestination]]:
        
        ...
    


