

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationAttachmentsConfigurationArgs', 'ApplicationAttachmentsConfigurationArgsDict', 'ApplicationEncryptionConfigurationArgs', 'ApplicationEncryptionConfigurationArgsDict', 'ApplicationTimeoutsArgs', 'ApplicationTimeoutsArgsDict']
class ApplicationAttachmentsConfigurationArgsDict(TypedDict):
    attachments_control_mode: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationAttachmentsConfigurationArgs:
    def __init__(__self__, *, attachments_control_mode: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentsControlMode")
    def attachments_control_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attachments_control_mode.setter
    def attachments_control_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationEncryptionConfigurationArgsDict(TypedDict):
    kms_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


