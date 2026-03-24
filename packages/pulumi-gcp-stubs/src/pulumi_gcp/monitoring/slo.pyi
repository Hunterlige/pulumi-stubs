

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
__all__ = ['SloArgs', 'Slo']
@pulumi.input_type
class SloArgs:
    def __init__(__self__, *, goal: pulumi.Input[_builtins.float], service: pulumi.Input[_builtins.str], basic_sli: Optional[pulumi.Input[SloBasicSliArgs]] = ..., calendar_period: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., request_based_sli: Optional[pulumi.Input[SloRequestBasedSliArgs]] = ..., rolling_period_days: Optional[pulumi.Input[_builtins.int]] = ..., slo_id: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., windows_based_sli: Optional[pulumi.Input[SloWindowsBasedSliArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def goal(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @goal.setter
    def goal(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicSli")
    def basic_sli(self) -> Optional[pulumi.Input[SloBasicSliArgs]]:
        
        ...
    
    @basic_sli.setter
    def basic_sli(self, value: Optional[pulumi.Input[SloBasicSliArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @calendar_period.setter
    def calendar_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBasedSli")
    def request_based_sli(self) -> Optional[pulumi.Input[SloRequestBasedSliArgs]]:
        
        ...
    
    @request_based_sli.setter
    def request_based_sli(self, value: Optional[pulumi.Input[SloRequestBasedSliArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingPeriodDays")
    def rolling_period_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rolling_period_days.setter
    def rolling_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sloId")
    def slo_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @slo_id.setter
    def slo_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_labels.setter
    def user_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsBasedSli")
    def windows_based_sli(self) -> Optional[pulumi.Input[SloWindowsBasedSliArgs]]:
        
        ...
    
    @windows_based_sli.setter
    def windows_based_sli(self, value: Optional[pulumi.Input[SloWindowsBasedSliArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _SloState:
    def __init__(__self__, *, basic_sli: Optional[pulumi.Input[SloBasicSliArgs]] = ..., calendar_period: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., goal: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., request_based_sli: Optional[pulumi.Input[SloRequestBasedSliArgs]] = ..., rolling_period_days: Optional[pulumi.Input[_builtins.int]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., slo_id: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., windows_based_sli: Optional[pulumi.Input[SloWindowsBasedSliArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicSli")
    def basic_sli(self) -> Optional[pulumi.Input[SloBasicSliArgs]]:
        
        ...
    
    @basic_sli.setter
    def basic_sli(self, value: Optional[pulumi.Input[SloBasicSliArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @calendar_period.setter
    def calendar_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def goal(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @goal.setter
    def goal(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBasedSli")
    def request_based_sli(self) -> Optional[pulumi.Input[SloRequestBasedSliArgs]]:
        
        ...
    
    @request_based_sli.setter
    def request_based_sli(self, value: Optional[pulumi.Input[SloRequestBasedSliArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingPeriodDays")
    def rolling_period_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rolling_period_days.setter
    def rolling_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sloId")
    def slo_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @slo_id.setter
    def slo_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_labels.setter
    def user_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsBasedSli")
    def windows_based_sli(self) -> Optional[pulumi.Input[SloWindowsBasedSliArgs]]:
        
        ...
    
    @windows_based_sli.setter
    def windows_based_sli(self, value: Optional[pulumi.Input[SloWindowsBasedSliArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:monitoring/slo:Slo")
class Slo(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., basic_sli: Optional[pulumi.Input[Union[SloBasicSliArgs, SloBasicSliArgsDict]]] = ..., calendar_period: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., goal: Optional[pulumi.Input[_builtins.float]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., request_based_sli: Optional[pulumi.Input[Union[SloRequestBasedSliArgs, SloRequestBasedSliArgsDict]]] = ..., rolling_period_days: Optional[pulumi.Input[_builtins.int]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., slo_id: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., windows_based_sli: Optional[pulumi.Input[Union[SloWindowsBasedSliArgs, SloWindowsBasedSliArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SloArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., basic_sli: Optional[pulumi.Input[Union[SloBasicSliArgs, SloBasicSliArgsDict]]] = ..., calendar_period: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., goal: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., request_based_sli: Optional[pulumi.Input[Union[SloRequestBasedSliArgs, SloRequestBasedSliArgsDict]]] = ..., rolling_period_days: Optional[pulumi.Input[_builtins.int]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., slo_id: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., windows_based_sli: Optional[pulumi.Input[Union[SloWindowsBasedSliArgs, SloWindowsBasedSliArgsDict]]] = ...) -> Slo:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicSli")
    def basic_sli(self) -> pulumi.Output[Optional[outputs.SloBasicSli]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def goal(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBasedSli")
    def request_based_sli(self) -> pulumi.Output[Optional[outputs.SloRequestBasedSli]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingPeriodDays")
    def rolling_period_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sloId")
    def slo_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsBasedSli")
    def windows_based_sli(self) -> pulumi.Output[Optional[outputs.SloWindowsBasedSli]]:
        
        ...
    


