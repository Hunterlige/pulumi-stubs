

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
__all__ = ['AllowedImagesSettingsArgs', 'AllowedImagesSettings']
@pulumi.input_type
class AllowedImagesSettingsArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], image_criterions: Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageCriterions")
    def image_criterions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]]:
        
        ...
    
    @image_criterions.setter
    def image_criterions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AllowedImagesSettingsState:
    def __init__(__self__, *, image_criterions: Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageCriterions")
    def image_criterions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]]:
        
        ...
    
    @image_criterions.setter
    def image_criterions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AllowedImagesSettingsImageCriterionArgs]]]]): # -> None:
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
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AllowedImagesSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., image_criterions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AllowedImagesSettingsImageCriterionArgs, AllowedImagesSettingsImageCriterionArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AllowedImagesSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., image_criterions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AllowedImagesSettingsImageCriterionArgs, AllowedImagesSettingsImageCriterionArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> AllowedImagesSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageCriterions")
    def image_criterions(self) -> pulumi.Output[Optional[Sequence[outputs.AllowedImagesSettingsImageCriterion]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


