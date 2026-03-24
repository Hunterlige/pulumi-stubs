

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPlaceIndexResult', 'AwaitableGetPlaceIndexResult', 'get_place_index', 'get_place_index_output']
@pulumi.output_type
class GetPlaceIndexResult:
    
    def __init__(__self__, create_time=..., data_source=..., data_source_configurations=..., description=..., id=..., index_arn=..., index_name=..., region=..., tags=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfigurations")
    def data_source_configurations(self) -> Sequence[outputs.GetPlaceIndexDataSourceConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPlaceIndexResult(GetPlaceIndexResult):
    def __await__(self): # -> Generator[Never, Any, GetPlaceIndexResult]:
        ...
    


def get_place_index(index_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPlaceIndexResult:
    
    ...

def get_place_index_output(index_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPlaceIndexResult]:
    
    ...

