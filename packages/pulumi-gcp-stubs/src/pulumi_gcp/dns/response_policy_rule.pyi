

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResponsePolicyRuleArgs', 'ResponsePolicyRule']
@pulumi.input_type
class ResponsePolicyRuleArgs:
    def __init__(__self__, *, dns_name: pulumi.Input[_builtins.str], response_policy: pulumi.Input[_builtins.str], rule_name: pulumi.Input[_builtins.str], behavior: Optional[pulumi.Input[_builtins.str]] = ..., local_data: Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicy")
    def response_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @response_policy.setter
    def response_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @behavior.setter
    def behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localData")
    def local_data(self) -> Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]]:
        
        ...
    
    @local_data.setter
    def local_data(self, value: Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResponsePolicyRuleState:
    def __init__(__self__, *, behavior: Optional[pulumi.Input[_builtins.str]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., local_data: Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @behavior.setter
    def behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localData")
    def local_data(self) -> Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]]:
        
        ...
    
    @local_data.setter
    def local_data(self, value: Optional[pulumi.Input[ResponsePolicyRuleLocalDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicy")
    def response_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_policy.setter
    def response_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dns/responsePolicyRule:ResponsePolicyRule")
class ResponsePolicyRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., behavior: Optional[pulumi.Input[_builtins.str]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., local_data: Optional[pulumi.Input[Union[ResponsePolicyRuleLocalDataArgs, ResponsePolicyRuleLocalDataArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResponsePolicyRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., behavior: Optional[pulumi.Input[_builtins.str]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., local_data: Optional[pulumi.Input[Union[ResponsePolicyRuleLocalDataArgs, ResponsePolicyRuleLocalDataArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ResponsePolicyRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localData")
    def local_data(self) -> pulumi.Output[Optional[outputs.ResponsePolicyRuleLocalData]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicy")
    def response_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


