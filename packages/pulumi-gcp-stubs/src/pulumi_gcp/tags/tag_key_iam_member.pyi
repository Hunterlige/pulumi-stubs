

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
__all__ = ['TagKeyIamMemberArgs', 'TagKeyIamMember']
@pulumi.input_type
class TagKeyIamMemberArgs:
    def __init__(__self__, *, member: pulumi.Input[_builtins.str], role: pulumi.Input[_builtins.str], tag_key: pulumi.Input[_builtins.str], condition: Optional[pulumi.Input[TagKeyIamMemberConditionArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tag_key.setter
    def tag_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[TagKeyIamMemberConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[TagKeyIamMemberConditionArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TagKeyIamMemberState:
    def __init__(__self__, *, condition: Optional[pulumi.Input[TagKeyIamMemberConditionArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., tag_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[TagKeyIamMemberConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[TagKeyIamMemberConditionArgs]]): # -> None:
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
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_key.setter
    def tag_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:tags/tagKeyIamMember:TagKeyIamMember")
class TagKeyIamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[TagKeyIamMemberConditionArgs, TagKeyIamMemberConditionArgsDict]]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., tag_key: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TagKeyIamMemberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[TagKeyIamMemberConditionArgs, TagKeyIamMemberConditionArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., member: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., tag_key: Optional[pulumi.Input[_builtins.str]] = ...) -> TagKeyIamMember:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.TagKeyIamMemberCondition]]:
        
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
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


