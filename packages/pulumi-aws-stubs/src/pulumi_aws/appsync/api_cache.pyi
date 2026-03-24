

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiCacheArgs', 'ApiCache']
@pulumi.input_type
class ApiCacheArgs:
    def __init__(__self__, *, api_caching_behavior: pulumi.Input[_builtins.str], api_id: pulumi.Input[_builtins.str], ttl: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str], at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiCachingBehavior")
    def api_caching_behavior(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_caching_behavior.setter
    def api_caching_behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_encryption_enabled.setter
    def transit_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ApiCacheState:
    def __init__(__self__, *, api_caching_behavior: Optional[pulumi.Input[_builtins.str]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ttl: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiCachingBehavior")
    def api_caching_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_caching_behavior.setter
    def api_caching_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_encryption_enabled.setter
    def transit_encryption_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:appsync/apiCache:ApiCache")
class ApiCache(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_caching_behavior: Optional[pulumi.Input[_builtins.str]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ttl: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApiCacheArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_caching_behavior: Optional[pulumi.Input[_builtins.str]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ttl: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> ApiCache:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiCachingBehavior")
    def api_caching_behavior(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


