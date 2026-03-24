

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
__all__ = ['NotificationChannelArgs', 'NotificationChannel']
@pulumi.input_type
class NotificationChannelArgs:
    def __init__(__self__, *, sns: pulumi.Input[NotificationChannelSnsArgs], filters: Optional[pulumi.Input[NotificationChannelFiltersArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> pulumi.Input[NotificationChannelSnsArgs]:
        
        ...
    
    @sns.setter
    def sns(self, value: pulumi.Input[NotificationChannelSnsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[NotificationChannelFiltersArgs]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[NotificationChannelFiltersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NotificationChannelState:
    def __init__(__self__, *, filters: Optional[pulumi.Input[NotificationChannelFiltersArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns: Optional[pulumi.Input[NotificationChannelSnsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[NotificationChannelFiltersArgs]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[NotificationChannelFiltersArgs]]): # -> None:
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
    def sns(self) -> Optional[pulumi.Input[NotificationChannelSnsArgs]]:
        
        ...
    
    @sns.setter
    def sns(self, value: Optional[pulumi.Input[NotificationChannelSnsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class NotificationChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., filters: Optional[pulumi.Input[Union[NotificationChannelFiltersArgs, NotificationChannelFiltersArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns: Optional[pulumi.Input[Union[NotificationChannelSnsArgs, NotificationChannelSnsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NotificationChannelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., filters: Optional[pulumi.Input[Union[NotificationChannelFiltersArgs, NotificationChannelFiltersArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns: Optional[pulumi.Input[Union[NotificationChannelSnsArgs, NotificationChannelSnsArgsDict]]] = ...) -> NotificationChannel:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[outputs.NotificationChannelFilters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sns(self) -> pulumi.Output[outputs.NotificationChannelSns]:
        
        ...
    


