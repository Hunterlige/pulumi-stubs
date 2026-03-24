

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRestApiResult', 'AwaitableGetRestApiResult', 'get_rest_api', 'get_rest_api_output']
@pulumi.output_type
class GetRestApiResult:
    
    def __init__(__self__, api_key_source=..., arn=..., binary_media_types=..., description=..., endpoint_configurations=..., execution_arn=..., id=..., minimum_compression_size=..., name=..., policy=..., region=..., root_resource_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySource")
    def api_key_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(self) -> Sequence[outputs.GetRestApiEndpointConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootResourceId")
    def root_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetRestApiResult(GetRestApiResult):
    def __await__(self): # -> Generator[Never, Any, GetRestApiResult]:
        ...
    


def get_rest_api(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRestApiResult:
    
    ...

def get_rest_api_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRestApiResult]:
    
    ...

