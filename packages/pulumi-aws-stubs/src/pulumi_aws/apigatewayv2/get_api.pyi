

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiResult', 'AwaitableGetApiResult', 'get_api', 'get_api_output']
@pulumi.output_type
class GetApiResult:
    
    def __init__(__self__, api_endpoint=..., api_id=..., api_key_selection_expression=..., arn=..., cors_configurations=..., description=..., disable_execute_api_endpoint=..., execution_arn=..., id=..., ip_address_type=..., name=..., protocol_type=..., region=..., route_selection_expression=..., tags=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfigurations")
    def cors_configurations(self) -> Sequence[outputs.GetApiCorsConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> _builtins.bool:
        
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
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetApiResult(GetApiResult):
    def __await__(self): # -> Generator[Never, Any, GetApiResult]:
        ...
    


def get_api(api_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiResult:
    
    ...

def get_api_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiResult]:
    
    ...

