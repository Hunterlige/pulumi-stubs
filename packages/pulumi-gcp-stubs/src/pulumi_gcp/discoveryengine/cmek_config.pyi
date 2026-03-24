

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
__all__ = ['CmekConfigArgs', 'CmekConfig']
@pulumi.input_type
class CmekConfigArgs:
    def __init__(__self__, *, cmek_config_id: pulumi.Input[_builtins.str], kms_key: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ..., set_default: Optional[pulumi.Input[_builtins.bool]] = ..., single_region_keys: Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfigId")
    def cmek_config_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cmek_config_id.setter
    def cmek_config_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setDefault")
    def set_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @set_default.setter
    def set_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleRegionKeys")
    def single_region_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]]:
        
        ...
    
    @single_region_keys.setter
    def single_region_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CmekConfigState:
    def __init__(__self__, *, cmek_config_id: Optional[pulumi.Input[_builtins.str]] = ..., is_default: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_version: Optional[pulumi.Input[_builtins.str]] = ..., last_rotation_timestamp_micros: Optional[pulumi.Input[_builtins.int]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notebooklm_state: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., set_default: Optional[pulumi.Input[_builtins.bool]] = ..., single_region_keys: Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfigId")
    def cmek_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cmek_config_id.setter
    def cmek_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version.setter
    def kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRotationTimestampMicros")
    def last_rotation_timestamp_micros(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @last_rotation_timestamp_micros.setter
    def last_rotation_timestamp_micros(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="notebooklmState")
    def notebooklm_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notebooklm_state.setter
    def notebooklm_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setDefault")
    def set_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @set_default.setter
    def set_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleRegionKeys")
    def single_region_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]]:
        
        ...
    
    @single_region_keys.setter
    def single_region_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CmekConfigSingleRegionKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/cmekConfig:CmekConfig")
class CmekConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cmek_config_id: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., set_default: Optional[pulumi.Input[_builtins.bool]] = ..., single_region_keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CmekConfigSingleRegionKeyArgs, CmekConfigSingleRegionKeyArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CmekConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cmek_config_id: Optional[pulumi.Input[_builtins.str]] = ..., is_default: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_version: Optional[pulumi.Input[_builtins.str]] = ..., last_rotation_timestamp_micros: Optional[pulumi.Input[_builtins.int]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notebooklm_state: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., set_default: Optional[pulumi.Input[_builtins.bool]] = ..., single_region_keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CmekConfigSingleRegionKeyArgs, CmekConfigSingleRegionKeyArgsDict]]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> CmekConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekConfigId")
    def cmek_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRotationTimestampMicros")
    def last_rotation_timestamp_micros(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter(name="notebooklmState")
    def notebooklm_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="setDefault")
    def set_default(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleRegionKeys")
    def single_region_keys(self) -> pulumi.Output[Optional[Sequence[outputs.CmekConfigSingleRegionKey]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


