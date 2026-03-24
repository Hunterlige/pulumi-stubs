

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
__all__ = ['FieldLevelEncryptionProfileArgs', 'FieldLevelEncryptionProfile']
@pulumi.input_type
class FieldLevelEncryptionProfileArgs:
    def __init__(__self__, *, encryption_entities: pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs], comment: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionEntities")
    def encryption_entities(self) -> pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs]:
        
        ...
    
    @encryption_entities.setter
    def encryption_entities(self, value: pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FieldLevelEncryptionProfileState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_entities: Optional[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @caller_reference.setter
    def caller_reference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionEntities")
    def encryption_entities(self) -> Optional[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs]]:
        
        ...
    
    @encryption_entities.setter
    def encryption_entities(self, value: Optional[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesArgs]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FieldLevelEncryptionProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_entities: Optional[pulumi.Input[Union[FieldLevelEncryptionProfileEncryptionEntitiesArgs, FieldLevelEncryptionProfileEncryptionEntitiesArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FieldLevelEncryptionProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., encryption_entities: Optional[pulumi.Input[Union[FieldLevelEncryptionProfileEncryptionEntitiesArgs, FieldLevelEncryptionProfileEncryptionEntitiesArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> FieldLevelEncryptionProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionEntities")
    def encryption_entities(self) -> pulumi.Output[outputs.FieldLevelEncryptionProfileEncryptionEntities]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


