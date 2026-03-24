

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
__all__ = ['AttestorIamMemberArgs', 'AttestorIamMember']
@pulumi.input_type
class AttestorIamMemberArgs:
    def __init__(__self__, *, attestor: pulumi.Input[_builtins.str], member: pulumi.Input[_builtins.str], role: pulumi.Input[_builtins.str], condition: Optional[pulumi.Input[AttestorIamMemberConditionArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attestor(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attestor.setter
    def attestor(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @member.setter
    def member(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[AttestorIamMemberConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[AttestorIamMemberConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AttestorIamMemberState:
    def __init__(__self__, *, attestor: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[AttestorIamMemberConditionArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attestor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attestor.setter
    def attestor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[AttestorIamMemberConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[AttestorIamMemberConditionArgs]]): # -> None:
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
    def member(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @member.setter
    def member(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AttestorIamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attestor: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[AttestorIamMemberConditionArgs, AttestorIamMemberConditionArgsDict]]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AttestorIamMemberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attestor: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[AttestorIamMemberConditionArgs, AttestorIamMemberConditionArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> AttestorIamMember:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attestor(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.AttestorIamMemberCondition]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


