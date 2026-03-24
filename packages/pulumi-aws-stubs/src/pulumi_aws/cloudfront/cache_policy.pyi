

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
__all__ = ['CachePolicyArgs', 'CachePolicy']
@pulumi.input_type
class CachePolicyArgs:
    def __init__(__self__, *, parameters_in_cache_key_and_forwarded_to_origin: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs], comment: Optional[pulumi.Input[_builtins.str]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersInCacheKeyAndForwardedToOrigin")
    def parameters_in_cache_key_and_forwarded_to_origin(self) -> pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs]:
        
        ...
    
    @parameters_in_cache_key_and_forwarded_to_origin.setter
    def parameters_in_cache_key_and_forwarded_to_origin(self, value: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ttl.setter
    def min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CachePolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters_in_cache_key_and_forwarded_to_origin: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ttl.setter
    def min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersInCacheKeyAndForwardedToOrigin")
    def parameters_in_cache_key_and_forwarded_to_origin(self) -> Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs]]:
        
        ...
    
    @parameters_in_cache_key_and_forwarded_to_origin.setter
    def parameters_in_cache_key_and_forwarded_to_origin(self, value: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudfront/cachePolicy:CachePolicy")
class CachePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters_in_cache_key_and_forwarded_to_origin: Optional[pulumi.Input[Union[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs, CachePolicyParametersInCacheKeyAndForwardedToOriginArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CachePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters_in_cache_key_and_forwarded_to_origin: Optional[pulumi.Input[Union[CachePolicyParametersInCacheKeyAndForwardedToOriginArgs, CachePolicyParametersInCacheKeyAndForwardedToOriginArgsDict]]] = ...) -> CachePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersInCacheKeyAndForwardedToOrigin")
    def parameters_in_cache_key_and_forwarded_to_origin(self) -> pulumi.Output[outputs.CachePolicyParametersInCacheKeyAndForwardedToOrigin]:
        
        ...
    


