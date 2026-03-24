

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ObjectACLArgs', 'ObjectACL']
@pulumi.input_type
class ObjectACLArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], object: pulumi.Input[_builtins.str], predefined_acl: Optional[pulumi.Input[_builtins.str]] = ..., role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @predefined_acl.setter
    def predefined_acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ObjectACLState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., object: Optional[pulumi.Input[_builtins.str]] = ..., predefined_acl: Optional[pulumi.Input[_builtins.str]] = ..., role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object.setter
    def object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @predefined_acl.setter
    def predefined_acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:storage/objectACL:ObjectACL")
class ObjectACL(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., object: Optional[pulumi.Input[_builtins.str]] = ..., predefined_acl: Optional[pulumi.Input[_builtins.str]] = ..., role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ObjectACLArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., object: Optional[pulumi.Input[_builtins.str]] = ..., predefined_acl: Optional[pulumi.Input[_builtins.str]] = ..., role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> ObjectACL:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


