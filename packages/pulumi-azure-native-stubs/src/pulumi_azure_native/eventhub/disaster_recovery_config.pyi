

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DisasterRecoveryConfigArgs', 'DisasterRecoveryConfig']
@pulumi.input_type
class DisasterRecoveryConfigArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], alias: Optional[pulumi.Input[_builtins.str]] = ..., alternate_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alternate_name.setter
    def alternate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerNamespace")
    def partner_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_namespace.setter
    def partner_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventhub:DisasterRecoveryConfig")
class DisasterRecoveryConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., alternate_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_namespace: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DisasterRecoveryConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DisasterRecoveryConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="partnerNamespace")
    def partner_namespace(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingReplicationOperationsCount")
    def pending_replication_operations_count(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


