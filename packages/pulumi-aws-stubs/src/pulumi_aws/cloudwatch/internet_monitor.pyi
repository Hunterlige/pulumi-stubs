

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
__all__ = ['InternetMonitorArgs', 'InternetMonitor']
@pulumi.input_type
class InternetMonitorArgs:
    def __init__(__self__, *, monitor_name: pulumi.Input[_builtins.str], health_events_config: Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]] = ..., internet_measurements_log_delivery: Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]] = ..., max_city_networks_to_monitor: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_percentage_to_monitor: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthEventsConfig")
    def health_events_config(self) -> Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]]:
        
        ...
    
    @health_events_config.setter
    def health_events_config(self, value: Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(self) -> Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]]:
        
        ...
    
    @internet_measurements_log_delivery.setter
    def internet_measurements_log_delivery(self, value: Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_city_networks_to_monitor.setter
    def max_city_networks_to_monitor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @traffic_percentage_to_monitor.setter
    def traffic_percentage_to_monitor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _InternetMonitorState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., health_events_config: Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]] = ..., internet_measurements_log_delivery: Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]] = ..., max_city_networks_to_monitor: Optional[pulumi.Input[_builtins.int]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_percentage_to_monitor: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthEventsConfig")
    def health_events_config(self) -> Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]]:
        
        ...
    
    @health_events_config.setter
    def health_events_config(self, value: Optional[pulumi.Input[InternetMonitorHealthEventsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(self) -> Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]]:
        
        ...
    
    @internet_measurements_log_delivery.setter
    def internet_measurements_log_delivery(self, value: Optional[pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_city_networks_to_monitor.setter
    def max_city_networks_to_monitor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitor_name.setter
    def monitor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @traffic_percentage_to_monitor.setter
    def traffic_percentage_to_monitor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/internetMonitor:InternetMonitor")
class InternetMonitor(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., health_events_config: Optional[pulumi.Input[Union[InternetMonitorHealthEventsConfigArgs, InternetMonitorHealthEventsConfigArgsDict]]] = ..., internet_measurements_log_delivery: Optional[pulumi.Input[Union[InternetMonitorInternetMeasurementsLogDeliveryArgs, InternetMonitorInternetMeasurementsLogDeliveryArgsDict]]] = ..., max_city_networks_to_monitor: Optional[pulumi.Input[_builtins.int]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_percentage_to_monitor: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InternetMonitorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., health_events_config: Optional[pulumi.Input[Union[InternetMonitorHealthEventsConfigArgs, InternetMonitorHealthEventsConfigArgsDict]]] = ..., internet_measurements_log_delivery: Optional[pulumi.Input[Union[InternetMonitorInternetMeasurementsLogDeliveryArgs, InternetMonitorInternetMeasurementsLogDeliveryArgsDict]]] = ..., max_city_networks_to_monitor: Optional[pulumi.Input[_builtins.int]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., traffic_percentage_to_monitor: Optional[pulumi.Input[_builtins.int]] = ...) -> InternetMonitor:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthEventsConfig")
    def health_events_config(self) -> pulumi.Output[Optional[outputs.InternetMonitorHealthEventsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(self) -> pulumi.Output[Optional[outputs.InternetMonitorInternetMeasurementsLogDelivery]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


