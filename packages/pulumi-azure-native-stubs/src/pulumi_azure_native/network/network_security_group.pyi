

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
__all__ = ['NetworkSecurityGroupInitArgs', 'NetworkSecurityGroup']
@pulumi.input_type
class NetworkSecurityGroupInitArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], flush_connection: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_security_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityRuleArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flushConnection")
    def flush_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @flush_connection.setter
    def flush_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupName")
    def network_security_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_security_group_name.setter
    def network_security_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityRuleArgs]]]]:
        
        ...
    
    @security_rules.setter
    def security_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:NetworkSecurityGroup")
class NetworkSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., flush_connection: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_security_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityRuleArgs, SecurityRuleArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkSecurityGroupInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NetworkSecurityGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSecurityRules")
    def default_security_rules(self) -> pulumi.Output[Sequence[outputs.SecurityRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowLogs")
    def flow_logs(self) -> pulumi.Output[Sequence[outputs.FlowLogResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flushConnection")
    def flush_connection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence[outputs.NetworkInterfaceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> pulumi.Output[Optional[Sequence[outputs.SecurityRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence[outputs.SubnetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


