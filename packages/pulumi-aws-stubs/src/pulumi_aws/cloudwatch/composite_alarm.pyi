

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
__all__ = ['CompositeAlarmArgs', 'CompositeAlarm']
@pulumi.input_type
class CompositeAlarmArgs:
    def __init__(__self__, *, alarm_name: pulumi.Input[_builtins.str], alarm_rule: pulumi.Input[_builtins.str], actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., actions_suppressor: Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]] = ..., alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., alarm_description: Optional[pulumi.Input[_builtins.str]] = ..., insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alarm_name.setter
    def alarm_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alarm_rule.setter
    def alarm_rule(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsSuppressor")
    def actions_suppressor(self) -> Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]]:
        
        ...
    
    @actions_suppressor.setter
    def actions_suppressor(self, value: Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @alarm_actions.setter
    def alarm_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @insufficient_data_actions.setter
    def insufficient_data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ok_actions.setter
    def ok_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CompositeAlarmState:
    def __init__(__self__, *, actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., actions_suppressor: Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]] = ..., alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., alarm_description: Optional[pulumi.Input[_builtins.str]] = ..., alarm_name: Optional[pulumi.Input[_builtins.str]] = ..., alarm_rule: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsSuppressor")
    def actions_suppressor(self) -> Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]]:
        
        ...
    
    @actions_suppressor.setter
    def actions_suppressor(self, value: Optional[pulumi.Input[CompositeAlarmActionsSuppressorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @alarm_actions.setter
    def alarm_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alarm_name.setter
    def alarm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alarm_rule.setter
    def alarm_rule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @insufficient_data_actions.setter
    def insufficient_data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ok_actions.setter
    def ok_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    


@pulumi.type_token("aws:cloudwatch/compositeAlarm:CompositeAlarm")
class CompositeAlarm(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., actions_suppressor: Optional[pulumi.Input[Union[CompositeAlarmActionsSuppressorArgs, CompositeAlarmActionsSuppressorArgsDict]]] = ..., alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., alarm_description: Optional[pulumi.Input[_builtins.str]] = ..., alarm_name: Optional[pulumi.Input[_builtins.str]] = ..., alarm_rule: Optional[pulumi.Input[_builtins.str]] = ..., insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CompositeAlarmArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., actions_suppressor: Optional[pulumi.Input[Union[CompositeAlarmActionsSuppressorArgs, CompositeAlarmActionsSuppressorArgsDict]]] = ..., alarm_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., alarm_description: Optional[pulumi.Input[_builtins.str]] = ..., alarm_name: Optional[pulumi.Input[_builtins.str]] = ..., alarm_rule: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., insufficient_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> CompositeAlarm:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsSuppressor")
    def actions_suppressor(self) -> pulumi.Output[Optional[outputs.CompositeAlarmActionsSuppressor]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


