

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FolderSettingsArgs', 'FolderSettings']
@pulumi.input_type
class FolderSettingsArgs:
    def __init__(__self__, *, folder: pulumi.Input[_builtins.str], disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FolderSettingsState:
    def __init__(__self__, *, disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., logging_service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_service_account_id.setter
    def kms_service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_service_account_id.setter
    def logging_service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:logging/folderSettings:FolderSettings")
class FolderSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FolderSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., logging_service_account_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[_builtins.str]] = ...) -> FolderSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


