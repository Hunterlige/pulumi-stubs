

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
__all__ = ['UserRuleCollectionArgs', 'UserRuleCollection']
@pulumi.input_type
class UserRuleCollectionArgs:
    def __init__(__self__, *, applies_to_groups: pulumi.Input[Sequence[pulumi.Input[NetworkManagerSecurityGroupItemArgs]]], configuration_name: pulumi.Input[_builtins.str], network_manager_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Input[Sequence[pulumi.Input[NetworkManagerSecurityGroupItemArgs]]]:
        
        ...
    
    @applies_to_groups.setter
    def applies_to_groups(self, value: pulumi.Input[Sequence[pulumi.Input[NetworkManagerSecurityGroupItemArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_collection_name.setter
    def rule_collection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:UserRuleCollection")
class UserRuleCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., applies_to_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkManagerSecurityGroupItemArgs, NetworkManagerSecurityGroupItemArgsDict]]]]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserRuleCollectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> UserRuleCollection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Output[Sequence[outputs.NetworkManagerSecurityGroupItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    


