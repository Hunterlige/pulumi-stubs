

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceMetadataDefaultsArgs', 'InstanceMetadataDefaults']
@pulumi.input_type
class InstanceMetadataDefaultsArgs:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceMetadataDefaultsState:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InstanceMetadataDefaults(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[InstanceMetadataDefaultsArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceMetadataDefaults:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


