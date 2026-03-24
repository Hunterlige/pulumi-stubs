

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
__all__ = ['RegistryScanningConfigurationArgs', 'RegistryScanningConfiguration']
@pulumi.input_type
class RegistryScanningConfigurationArgs:
    def __init__(__self__, *, scan_type: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scan_type.setter
    def scan_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _RegistryScanningConfigurationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., registry_id: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]] = ..., scan_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryScanningConfigurationRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scan_type.setter
    def scan_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegistryScanningConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegistryScanningConfigurationRuleArgs, RegistryScanningConfigurationRuleArgsDict]]]]] = ..., scan_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegistryScanningConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., registry_id: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegistryScanningConfigurationRuleArgs, RegistryScanningConfigurationRuleArgsDict]]]]] = ..., scan_type: Optional[pulumi.Input[_builtins.str]] = ...) -> RegistryScanningConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.RegistryScanningConfigurationRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


