

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGraphResourceGraphResult', 'AwaitableGetGraphResourceGraphResult', 'get_graph_resource_graph', 'get_graph_resource_graph_output']
@pulumi.output_type
class GetGraphResourceGraphResult:
    
    def __init__(__self__, azure_api_version=..., id=..., identity=..., location=..., name=..., options=..., resource=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.GraphResourceGetPropertiesResponseOptions]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.GraphResourceGetPropertiesResponseResource]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGraphResourceGraphResult(GetGraphResourceGraphResult):
    def __await__(self): # -> Generator[Never, Any, GetGraphResourceGraphResult]:
        ...
    


def get_graph_resource_graph(account_name: Optional[_builtins.str] = ..., graph_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGraphResourceGraphResult:
    
    ...

def get_graph_resource_graph_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., graph_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGraphResourceGraphResult]:
    
    ...

