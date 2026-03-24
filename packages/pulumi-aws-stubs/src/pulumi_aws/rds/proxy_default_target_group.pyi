

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
__all__ = ['ProxyDefaultTargetGroupArgs', 'ProxyDefaultTargetGroup']
@pulumi.input_type
class ProxyDefaultTargetGroupArgs:
    def __init__(__self__, *, db_proxy_name: pulumi.Input[_builtins.str], connection_pool_config: Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db_proxy_name.setter
    def db_proxy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]]:
        
        ...
    
    @connection_pool_config.setter
    def connection_pool_config(self, value: Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ProxyDefaultTargetGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_config: Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]] = ..., db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]]:
        
        ...
    
    @connection_pool_config.setter
    def connection_pool_config(self, value: Optional[pulumi.Input[ProxyDefaultTargetGroupConnectionPoolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_proxy_name.setter
    def db_proxy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ProxyDefaultTargetGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_pool_config: Optional[pulumi.Input[Union[ProxyDefaultTargetGroupConnectionPoolConfigArgs, ProxyDefaultTargetGroupConnectionPoolConfigArgsDict]]] = ..., db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProxyDefaultTargetGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_config: Optional[pulumi.Input[Union[ProxyDefaultTargetGroupConnectionPoolConfigArgs, ProxyDefaultTargetGroupConnectionPoolConfigArgsDict]]] = ..., db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ProxyDefaultTargetGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> pulumi.Output[outputs.ProxyDefaultTargetGroupConnectionPoolConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


