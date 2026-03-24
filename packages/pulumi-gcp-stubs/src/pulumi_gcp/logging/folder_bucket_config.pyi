

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FolderBucketConfigArgs', 'FolderBucketConfig']
@pulumi.input_type
class FolderBucketConfigArgs:
    def __init__(__self__, *, bucket_id: pulumi.Input[_builtins.str], folder: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], cmek_settings: Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., index_configs: Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_id.setter
    def bucket_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(self) -> Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]]:
        
        ...
    
    @cmek_settings.setter
    def cmek_settings(self, value: Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]]:
        
        ...
    
    @index_configs.setter
    def index_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _FolderBucketConfigState:
    def __init__(__self__, *, bucket_id: Optional[pulumi.Input[_builtins.str]] = ..., cmek_settings: Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., index_configs: Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]] = ..., lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_id.setter
    def bucket_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(self) -> Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]]:
        
        ...
    
    @cmek_settings.setter
    def cmek_settings(self, value: Optional[pulumi.Input[FolderBucketConfigCmekSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]]:
        
        ...
    
    @index_configs.setter
    def index_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FolderBucketConfigIndexConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:logging/folderBucketConfig:FolderBucketConfig")
class FolderBucketConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket_id: Optional[pulumi.Input[_builtins.str]] = ..., cmek_settings: Optional[pulumi.Input[Union[FolderBucketConfigCmekSettingsArgs, FolderBucketConfigCmekSettingsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., index_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FolderBucketConfigIndexConfigArgs, FolderBucketConfigIndexConfigArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FolderBucketConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket_id: Optional[pulumi.Input[_builtins.str]] = ..., cmek_settings: Optional[pulumi.Input[Union[FolderBucketConfigCmekSettingsArgs, FolderBucketConfigCmekSettingsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., index_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FolderBucketConfigIndexConfigArgs, FolderBucketConfigIndexConfigArgsDict]]]]] = ..., lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ...) -> FolderBucketConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(self) -> pulumi.Output[Optional[outputs.FolderBucketConfigCmekSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(self) -> pulumi.Output[Sequence[outputs.FolderBucketConfigIndexConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


