

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataLakeConnectorTopicMapResult', 'AwaitableGetDataLakeConnectorTopicMapResult', 'get_data_lake_connector_topic_map', 'get_data_lake_connector_topic_map_output']
@pulumi.output_type
class GetDataLakeConnectorTopicMapResult:
    
    def __init__(__self__, azure_api_version=..., data_lake_connector_ref=..., extended_location=..., id=..., location=..., mapping=..., name=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLakeConnectorRef")
    def data_lake_connector_ref(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> outputs.DataLakeConnectorMapResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDataLakeConnectorTopicMapResult(GetDataLakeConnectorTopicMapResult):
    def __await__(self): # -> Generator[Never, Any, GetDataLakeConnectorTopicMapResult]:
        ...
    


def get_data_lake_connector_topic_map(data_lake_connector_name: Optional[_builtins.str] = ..., mq_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., topic_map_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataLakeConnectorTopicMapResult:
    
    ...

def get_data_lake_connector_topic_map_output(data_lake_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., mq_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_map_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataLakeConnectorTopicMapResult]:
    
    ...

