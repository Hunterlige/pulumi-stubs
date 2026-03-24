

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PermissionArgs', 'Permission']
@pulumi.input_type
class PermissionArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], certificate_authority_arn: pulumi.Input[_builtins.str], principal: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_account.setter
    def source_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PermissionState:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_account.setter
    def source_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:acmpca/permission:Permission")
class Permission(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PermissionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_account: Optional[pulumi.Input[_builtins.str]] = ...) -> Permission:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


