

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AlertRuleResourceArgs', 'AlertRuleResource']
@pulumi.input_type
class AlertRuleResourceArgs:
    def __init__(__self__, *, alert_rule_resource_id: pulumi.Input[_builtins.str], alert_rule_template_id: pulumi.Input[_builtins.str], alert_rule_template_version: pulumi.Input[_builtins.str], created_with_properties: pulumi.Input[Union[_builtins.str, AlertRuleCreationProperties]], creation_time: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], watcher_name: pulumi.Input[_builtins.str], alert_rule_resource_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alert_rule_resource_id.setter
    def alert_rule_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateId")
    def alert_rule_template_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alert_rule_template_id.setter
    def alert_rule_template_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alert_rule_template_version.setter
    def alert_rule_template_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdWithProperties")
    def created_with_properties(self) -> pulumi.Input[Union[_builtins.str, AlertRuleCreationProperties]]:
        
        ...
    
    @created_with_properties.setter
    def created_with_properties(self, value: pulumi.Input[Union[_builtins.str, AlertRuleCreationProperties]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watcherName")
    def watcher_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @watcher_name.setter
    def watcher_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleResourceName")
    def alert_rule_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_rule_resource_name.setter
    def alert_rule_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:databasewatcher:AlertRuleResource")
class AlertRuleResource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alert_rule_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., alert_rule_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., alert_rule_template_id: Optional[pulumi.Input[_builtins.str]] = ..., alert_rule_template_version: Optional[pulumi.Input[_builtins.str]] = ..., created_with_properties: Optional[pulumi.Input[Union[_builtins.str, AlertRuleCreationProperties]]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., watcher_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AlertRuleResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AlertRuleResource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateId")
    def alert_rule_template_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdWithProperties")
    def created_with_properties(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


