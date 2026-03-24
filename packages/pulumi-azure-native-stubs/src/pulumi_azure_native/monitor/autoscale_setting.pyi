

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoscaleSettingArgs', 'AutoscaleSetting']
@pulumi.input_type
class AutoscaleSettingArgs:
    def __init__(__self__, *, profiles: pulumi.Input[Sequence[pulumi.Input[AutoscaleProfileArgs]]], resource_group_name: pulumi.Input[_builtins.str], autoscale_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notifications: Optional[pulumi.Input[Sequence[pulumi.Input[AutoscaleNotificationArgs]]]] = ..., predictive_autoscale_policy: Optional[pulumi.Input[PredictiveAutoscalePolicyArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_resource_location: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> pulumi.Input[Sequence[pulumi.Input[AutoscaleProfileArgs]]]:
        
        ...
    
    @profiles.setter
    def profiles(self, value: pulumi.Input[Sequence[pulumi.Input[AutoscaleProfileArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettingName")
    def autoscale_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscale_setting_name.setter
    def autoscale_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutoscaleNotificationArgs]]]]:
        
        ...
    
    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AutoscaleNotificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictiveAutoscalePolicy")
    def predictive_autoscale_policy(self) -> Optional[pulumi.Input[PredictiveAutoscalePolicyArgs]]:
        
        ...
    
    @predictive_autoscale_policy.setter
    def predictive_autoscale_policy(self, value: Optional[pulumi.Input[PredictiveAutoscalePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceLocation")
    def target_resource_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_resource_location.setter
    def target_resource_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceUri")
    def target_resource_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_resource_uri.setter
    def target_resource_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:monitor:AutoscaleSetting")
class AutoscaleSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscale_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AutoscaleNotificationArgs, AutoscaleNotificationArgsDict]]]]] = ..., predictive_autoscale_policy: Optional[pulumi.Input[Union[PredictiveAutoscalePolicyArgs, PredictiveAutoscalePolicyArgsDict]]] = ..., profiles: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AutoscaleProfileArgs, AutoscaleProfileArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_resource_location: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AutoscaleSettingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AutoscaleSetting:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.AutoscaleSettingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


