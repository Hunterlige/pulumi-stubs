

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MaintenanceWindowArgs', 'MaintenanceWindow']
@pulumi.input_type
class MaintenanceWindowArgs:
    def __init__(__self__, *, cutoff: pulumi.Input[_builtins.int], duration: pulumi.Input[_builtins.int], schedule: pulumi.Input[_builtins.str], allow_unassociated_targets: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_offset: Optional[pulumi.Input[_builtins.int]] = ..., schedule_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cutoff(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @cutoff.setter
    def cutoff(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUnassociatedTargets")
    def allow_unassociated_targets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_unassociated_targets.setter
    def allow_unassociated_targets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="scheduleOffset")
    def schedule_offset(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @schedule_offset.setter
    def schedule_offset(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTimezone")
    def schedule_timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_timezone.setter
    def schedule_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _MaintenanceWindowState:
    def __init__(__self__, *, allow_unassociated_targets: Optional[pulumi.Input[_builtins.bool]] = ..., cutoff: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_offset: Optional[pulumi.Input[_builtins.int]] = ..., schedule_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUnassociatedTargets")
    def allow_unassociated_targets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_unassociated_targets.setter
    def allow_unassociated_targets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cutoff(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cutoff.setter
    def cutoff(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOffset")
    def schedule_offset(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @schedule_offset.setter
    def schedule_offset(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTimezone")
    def schedule_timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_timezone.setter
    def schedule_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:ssm/maintenanceWindow:MaintenanceWindow")
class MaintenanceWindow(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_unassociated_targets: Optional[pulumi.Input[_builtins.bool]] = ..., cutoff: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_offset: Optional[pulumi.Input[_builtins.int]] = ..., schedule_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MaintenanceWindowArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_unassociated_targets: Optional[pulumi.Input[_builtins.bool]] = ..., cutoff: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_offset: Optional[pulumi.Input[_builtins.int]] = ..., schedule_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> MaintenanceWindow:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUnassociatedTargets")
    def allow_unassociated_targets(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cutoff(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def schedule(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOffset")
    def schedule_offset(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTimezone")
    def schedule_timezone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


