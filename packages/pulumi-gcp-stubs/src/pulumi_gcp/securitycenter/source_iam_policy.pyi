

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SourceIamPolicyArgs', 'SourceIamPolicy']
@pulumi.input_type
class SourceIamPolicyArgs:
    def __init__(__self__, *, organization: pulumi.Input[_builtins.str], policy_data: pulumi.Input[_builtins.str], source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _SourceIamPolicyState:
    def __init__(__self__, *, etag: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:securitycenter/sourceIamPolicy:SourceIamPolicy")
class SourceIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SourceIamPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ...) -> SourceIamPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]:
        ...
    


