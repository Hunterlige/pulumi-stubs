

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainPolicyArgs', 'DomainPolicy']
@pulumi.input_type
class DomainPolicyArgs:
    def __init__(__self__, *, access_policies: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]], domain_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]:
        
        ...
    
    @access_policies.setter
    def access_policies(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainPolicyState:
    def __init__(__self__, *, access_policies: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:elasticsearch/domainPolicy:DomainPolicy")
class DomainPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_policies: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_policies: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> DomainPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


