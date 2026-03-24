

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CapacityPoolVolumeQuotaRuleArgs', 'CapacityPoolVolumeQuotaRule']
@pulumi.input_type
class CapacityPoolVolumeQuotaRuleArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], pool_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], volume_name: pulumi.Input[_builtins.str], location: Optional[pulumi.Input[_builtins.str]] = ..., quota_size_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ..., quota_target: Optional[pulumi.Input[_builtins.str]] = ..., quota_type: Optional[pulumi.Input[Union[_builtins.str, Type]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_quota_rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pool_name.setter
    def pool_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @quota_size_in_ki_bs.setter
    def quota_size_in_ki_bs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quota_target.setter
    def quota_target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> Optional[pulumi.Input[Union[_builtins.str, Type]]]:
        
        ...
    
    @quota_type.setter
    def quota_type(self, value: Optional[pulumi.Input[Union[_builtins.str, Type]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeQuotaRuleName")
    def volume_quota_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_quota_rule_name.setter
    def volume_quota_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:netapp:CapacityPoolVolumeQuotaRule")
class CapacityPoolVolumeQuotaRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., quota_size_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ..., quota_target: Optional[pulumi.Input[_builtins.str]] = ..., quota_type: Optional[pulumi.Input[Union[_builtins.str, Type]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_quota_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CapacityPoolVolumeQuotaRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CapacityPoolVolumeQuotaRule:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    


