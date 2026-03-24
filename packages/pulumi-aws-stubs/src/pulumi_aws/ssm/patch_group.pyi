

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PatchGroupArgs', 'PatchGroup']
@pulumi.input_type
class PatchGroupArgs:
    def __init__(__self__, *, baseline_id: pulumi.Input[_builtins.str], patch_group: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @baseline_id.setter
    def baseline_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchGroup")
    def patch_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @patch_group.setter
    def patch_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PatchGroupState:
    def __init__(__self__, *, baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., patch_group: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_id.setter
    def baseline_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchGroup")
    def patch_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @patch_group.setter
    def patch_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ssm/patchGroup:PatchGroup")
class PatchGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., patch_group: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PatchGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., baseline_id: Optional[pulumi.Input[_builtins.str]] = ..., patch_group: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> PatchGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchGroup")
    def patch_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


