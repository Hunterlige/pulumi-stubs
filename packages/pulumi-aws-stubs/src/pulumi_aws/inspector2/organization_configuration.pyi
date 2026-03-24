

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
__all__ = ['OrganizationConfigurationArgs', 'OrganizationConfiguration']
@pulumi.input_type
class OrganizationConfigurationArgs:
    def __init__(__self__, *, auto_enable: pulumi.Input[OrganizationConfigurationAutoEnableArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[OrganizationConfigurationAutoEnableArgs]:
        
        ...
    
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[OrganizationConfigurationAutoEnableArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationConfigurationState:
    def __init__(__self__, *, auto_enable: Optional[pulumi.Input[OrganizationConfigurationAutoEnableArgs]] = ..., max_account_limit_reached: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> Optional[pulumi.Input[OrganizationConfigurationAutoEnableArgs]]:
        
        ...
    
    @auto_enable.setter
    def auto_enable(self, value: Optional[pulumi.Input[OrganizationConfigurationAutoEnableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAccountLimitReached")
    def max_account_limit_reached(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @max_account_limit_reached.setter
    def max_account_limit_reached(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OrganizationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_enable: Optional[pulumi.Input[Union[OrganizationConfigurationAutoEnableArgs, OrganizationConfigurationAutoEnableArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., auto_enable: Optional[pulumi.Input[Union[OrganizationConfigurationAutoEnableArgs, OrganizationConfigurationAutoEnableArgsDict]]] = ..., max_account_limit_reached: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> OrganizationConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Output[outputs.OrganizationConfigurationAutoEnable]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAccountLimitReached")
    def max_account_limit_reached(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


