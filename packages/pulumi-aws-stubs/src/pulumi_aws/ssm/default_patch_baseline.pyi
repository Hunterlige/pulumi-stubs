

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DefaultPatchBaselineArgs', 'DefaultPatchBaseline']
@pulumi.input_type
class DefaultPatchBaselineArgs:
    def __init__(__self__, *, baseline_id: pulumi.Input[_builtins.str], operating_system: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @baseline_id.setter
    def baseline_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @operating_system.setter
    def operating_system(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DefaultPatchBaselineState:
    def __init__(__self__, *, baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., operating_system: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_id.setter
    def baseline_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ssm/defaultPatchBaseline:DefaultPatchBaseline")
class DefaultPatchBaseline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., operating_system: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefaultPatchBaselineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., operating_system: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> DefaultPatchBaseline:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


