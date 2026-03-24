

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RuleDeploymentArgs', 'RuleDeployment']
@pulumi.input_type
class RuleDeploymentArgs:
    def __init__(__self__, *, instance: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], rule: pulumi.Input[_builtins.str], alerting: Optional[pulumi.Input[_builtins.bool]] = ..., archived: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., run_frequency: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule.setter
    def rule(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerting(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @alerting.setter
    def alerting(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def archived(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @archived.setter
    def archived(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runFrequency")
    def run_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_frequency.setter
    def run_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RuleDeploymentState:
    def __init__(__self__, *, alerting: Optional[pulumi.Input[_builtins.bool]] = ..., archive_time: Optional[pulumi.Input[_builtins.str]] = ..., archived: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., execution_state: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., last_alert_status_change_time: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., producer_rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[_builtins.str]] = ..., run_frequency: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerting(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @alerting.setter
    def alerting(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveTime")
    def archive_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @archive_time.setter
    def archive_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def archived(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @archived.setter
    def archived(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRules")
    def consumer_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_rules.setter
    def consumer_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionState")
    def execution_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_state.setter
    def execution_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAlertStatusChangeTime")
    def last_alert_status_change_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_alert_status_change_time.setter
    def last_alert_status_change_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerRules")
    def producer_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @producer_rules.setter
    def producer_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runFrequency")
    def run_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_frequency.setter
    def run_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:chronicle/ruleDeployment:RuleDeployment")
class RuleDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alerting: Optional[pulumi.Input[_builtins.bool]] = ..., archived: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[_builtins.str]] = ..., run_frequency: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RuleDeploymentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alerting: Optional[pulumi.Input[_builtins.bool]] = ..., archive_time: Optional[pulumi.Input[_builtins.str]] = ..., archived: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., execution_state: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., last_alert_status_change_time: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., producer_rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[_builtins.str]] = ..., run_frequency: Optional[pulumi.Input[_builtins.str]] = ...) -> RuleDeployment:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerting(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveTime")
    def archive_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def archived(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRules")
    def consumer_rules(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionState")
    def execution_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAlertStatusChangeTime")
    def last_alert_status_change_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerRules")
    def producer_rules(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runFrequency")
    def run_frequency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


