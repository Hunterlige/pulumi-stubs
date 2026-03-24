

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SQuotaAdjusterSettingsArgs', 'SQuotaAdjusterSettings']
@pulumi.input_type
class SQuotaAdjusterSettingsArgs:
    def __init__(__self__, *, enablement: pulumi.Input[_builtins.str], parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enablement(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @enablement.setter
    def enablement(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SQuotaAdjusterSettingsState:
    def __init__(__self__, *, effective_container: Optional[pulumi.Input[_builtins.str]] = ..., effective_enablement: Optional[pulumi.Input[_builtins.str]] = ..., enablement: Optional[pulumi.Input[_builtins.str]] = ..., inherited: Optional[pulumi.Input[_builtins.bool]] = ..., inherited_from: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveContainer")
    @_utilities.deprecated(...)
    def effective_container(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_container.setter
    def effective_container(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEnablement")
    @_utilities.deprecated(...)
    def effective_enablement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_enablement.setter
    def effective_enablement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enablement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enablement.setter
    def enablement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def inherited(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inherited.setter
    def inherited(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritedFrom")
    def inherited_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inherited_from.setter
    def inherited_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SQuotaAdjusterSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., enablement: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SQuotaAdjusterSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., effective_container: Optional[pulumi.Input[_builtins.str]] = ..., effective_enablement: Optional[pulumi.Input[_builtins.str]] = ..., enablement: Optional[pulumi.Input[_builtins.str]] = ..., inherited: Optional[pulumi.Input[_builtins.bool]] = ..., inherited_from: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> SQuotaAdjusterSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveContainer")
    @_utilities.deprecated(...)
    def effective_container(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEnablement")
    @_utilities.deprecated(...)
    def effective_enablement(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enablement(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inherited(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritedFrom")
    def inherited_from(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


