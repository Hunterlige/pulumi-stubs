

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EgressPolicyArgs', 'EgressPolicy']
@pulumi.input_type
class EgressPolicyArgs:
    def __init__(__self__, *, egress_policy_name: pulumi.Input[_builtins.str], resource: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressPolicyName")
    def egress_policy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @egress_policy_name.setter
    def egress_policy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _EgressPolicyState:
    def __init__(__self__, *, access_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_policy_id.setter
    def access_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressPolicyName")
    def egress_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_policy_name.setter
    def egress_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:accesscontextmanager/egressPolicy:EgressPolicy")
class EgressPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., egress_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EgressPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ...) -> EgressPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressPolicyName")
    def egress_policy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


