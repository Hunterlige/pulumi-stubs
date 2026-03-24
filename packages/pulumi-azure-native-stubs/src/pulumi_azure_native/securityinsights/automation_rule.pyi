

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutomationRuleArgs', 'AutomationRule']
@pulumi.input_type
class AutomationRuleArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[Union[AutomationRuleAddIncidentTaskActionArgs, AutomationRuleModifyPropertiesActionArgs, AutomationRuleRunPlaybookActionArgs]]]], display_name: pulumi.Input[_builtins.str], order: pulumi.Input[_builtins.int], resource_group_name: pulumi.Input[_builtins.str], triggering_logic: pulumi.Input[AutomationRuleTriggeringLogicArgs], workspace_name: pulumi.Input[_builtins.str], automation_rule_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union[AutomationRuleAddIncidentTaskActionArgs, AutomationRuleModifyPropertiesActionArgs, AutomationRuleRunPlaybookActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union[AutomationRuleAddIncidentTaskActionArgs, AutomationRuleModifyPropertiesActionArgs, AutomationRuleRunPlaybookActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> pulumi.Input[AutomationRuleTriggeringLogicArgs]:
        
        ...
    
    @triggering_logic.setter
    def triggering_logic(self, value: pulumi.Input[AutomationRuleTriggeringLogicArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationRuleId")
    def automation_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @automation_rule_id.setter
    def automation_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:AutomationRule")
class AutomationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union[AutomationRuleAddIncidentTaskActionArgs, AutomationRuleAddIncidentTaskActionArgsDict], Union[AutomationRuleModifyPropertiesActionArgs, AutomationRuleModifyPropertiesActionArgsDict], Union[AutomationRuleRunPlaybookActionArgs, AutomationRuleRunPlaybookActionArgsDict]]]]]] = ..., automation_rule_id: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., triggering_logic: Optional[pulumi.Input[Union[AutomationRuleTriggeringLogicArgs, AutomationRuleTriggeringLogicArgsDict]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AutomationRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AutomationRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[outputs.ClientInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[outputs.ClientInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> pulumi.Output[outputs.AutomationRuleTriggeringLogicResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


