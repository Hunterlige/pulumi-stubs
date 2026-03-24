

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
__all__ = ['AddonsConfigArgs', 'AddonsConfig']
@pulumi.input_type
class AddonsConfigArgs:
    def __init__(__self__, *, org: pulumi.Input[_builtins.str], addons_config: Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org.setter
    def org(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]]:
        
        ...
    
    @addons_config.setter
    def addons_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AddonsConfigState:
    def __init__(__self__, *, addons_config: Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]] = ..., org: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]]:
        
        ...
    
    @addons_config.setter
    def addons_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org.setter
    def org(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/addonsConfig:AddonsConfig")
class AddonsConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., addons_config: Optional[pulumi.Input[Union[AddonsConfigAddonsConfigArgs, AddonsConfigAddonsConfigArgsDict]]] = ..., org: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AddonsConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., addons_config: Optional[pulumi.Input[Union[AddonsConfigAddonsConfigArgs, AddonsConfigAddonsConfigArgsDict]]] = ..., org: Optional[pulumi.Input[_builtins.str]] = ...) -> AddonsConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> pulumi.Output[Optional[outputs.AddonsConfigAddonsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


