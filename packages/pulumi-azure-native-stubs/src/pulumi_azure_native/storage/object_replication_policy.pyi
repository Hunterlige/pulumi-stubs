

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
__all__ = ['ObjectReplicationPolicyArgs', 'ObjectReplicationPolicy']
@pulumi.input_type
class ObjectReplicationPolicyArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], destination_account: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], source_account: pulumi.Input[_builtins.str], metrics: Optional[pulumi.Input[ObjectReplicationPolicyPropertiesMetricsArgs]] = ..., object_replication_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[ObjectReplicationPolicyRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_account.setter
    def destination_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_account.setter
    def source_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[ObjectReplicationPolicyPropertiesMetricsArgs]]:
        
        ...
    
    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[ObjectReplicationPolicyPropertiesMetricsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectReplicationPolicyId")
    def object_replication_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_replication_policy_id.setter
    def object_replication_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ObjectReplicationPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ObjectReplicationPolicyRuleArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:ObjectReplicationPolicy")
class ObjectReplicationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., destination_account: Optional[pulumi.Input[_builtins.str]] = ..., metrics: Optional[pulumi.Input[Union[ObjectReplicationPolicyPropertiesMetricsArgs, ObjectReplicationPolicyPropertiesMetricsArgsDict]]] = ..., object_replication_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ObjectReplicationPolicyRuleArgs, ObjectReplicationPolicyRuleArgsDict]]]]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ObjectReplicationPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ObjectReplicationPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional[outputs.ObjectReplicationPolicyPropertiesResponseMetrics]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.ObjectReplicationPolicyRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


