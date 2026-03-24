

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LongTermRetentionPolicyArgs', 'LongTermRetentionPolicy']
@pulumi.input_type
class LongTermRetentionPolicyArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], monthly_retention: Optional[pulumi.Input[_builtins.str]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., week_of_year: Optional[pulumi.Input[_builtins.int]] = ..., weekly_retention: Optional[pulumi.Input[_builtins.str]] = ..., yearly_retention: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monthly_retention.setter
    def monthly_retention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @week_of_year.setter
    def week_of_year(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @weekly_retention.setter
    def weekly_retention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @yearly_retention.setter
    def yearly_retention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:LongTermRetentionPolicy")
class LongTermRetentionPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., monthly_retention: Optional[pulumi.Input[_builtins.str]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., week_of_year: Optional[pulumi.Input[_builtins.int]] = ..., weekly_retention: Optional[pulumi.Input[_builtins.str]] = ..., yearly_retention: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LongTermRetentionPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LongTermRetentionPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


