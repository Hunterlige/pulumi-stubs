

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
__all__ = ['FieldLevelEncryptionConfigArgs', 'FieldLevelEncryptionConfig']
@pulumi.input_type
class FieldLevelEncryptionConfigArgs:
    def __init__(__self__, *, content_type_profile_config: pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs], query_arg_profile_config: pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs], comment: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypeProfileConfig")
    def content_type_profile_config(self) -> pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs]:
        
        ...
    
    @content_type_profile_config.setter
    def content_type_profile_config(self, value: pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgProfileConfig")
    def query_arg_profile_config(self) -> pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs]:
        
        ...
    
    @query_arg_profile_config.setter
    def query_arg_profile_config(self, value: pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FieldLevelEncryptionConfigState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., content_type_profile_config: Optional[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., query_arg_profile_config: Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="contentTypeProfileConfig")
    def content_type_profile_config(self) -> Optional[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs]]:
        
        ...
    
    @content_type_profile_config.setter
    def content_type_profile_config(self, value: Optional[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgProfileConfig")
    def query_arg_profile_config(self) -> Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs]]:
        
        ...
    
    @query_arg_profile_config.setter
    def query_arg_profile_config(self, value: Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FieldLevelEncryptionConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., content_type_profile_config: Optional[pulumi.Input[Union[FieldLevelEncryptionConfigContentTypeProfileConfigArgs, FieldLevelEncryptionConfigContentTypeProfileConfigArgsDict]]] = ..., query_arg_profile_config: Optional[pulumi.Input[Union[FieldLevelEncryptionConfigQueryArgProfileConfigArgs, FieldLevelEncryptionConfigQueryArgProfileConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FieldLevelEncryptionConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., caller_reference: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., content_type_profile_config: Optional[pulumi.Input[Union[FieldLevelEncryptionConfigContentTypeProfileConfigArgs, FieldLevelEncryptionConfigContentTypeProfileConfigArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., query_arg_profile_config: Optional[pulumi.Input[Union[FieldLevelEncryptionConfigQueryArgProfileConfigArgs, FieldLevelEncryptionConfigQueryArgProfileConfigArgsDict]]] = ...) -> FieldLevelEncryptionConfig:
        
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
    @pulumi.getter(name="contentTypeProfileConfig")
    def content_type_profile_config(self) -> pulumi.Output[outputs.FieldLevelEncryptionConfigContentTypeProfileConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgProfileConfig")
    def query_arg_profile_config(self) -> pulumi.Output[outputs.FieldLevelEncryptionConfigQueryArgProfileConfig]:
        
        ...
    


