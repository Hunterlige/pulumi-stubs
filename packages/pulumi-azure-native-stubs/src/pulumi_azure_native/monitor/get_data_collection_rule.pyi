

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataCollectionRuleResult', 'AwaitableGetDataCollectionRuleResult', 'get_data_collection_rule', 'get_data_collection_rule_output']
@pulumi.output_type
class GetDataCollectionRuleResult:
    
    def __init__(__self__, azure_api_version=..., data_collection_endpoint_id=..., data_flows=..., data_sources=..., description=..., destinations=..., etag=..., id=..., identity=..., immutable_id=..., kind=..., location=..., metadata=..., name=..., provisioning_state=..., stream_declarations=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointId")
    def data_collection_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFlows")
    def data_flows(self) -> Optional[Sequence[outputs.DataFlowResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[outputs.DataCollectionRuleResponseDataSources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[outputs.DataCollectionRuleResponseDestinations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.DataCollectionRuleResourceResponseIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.DataCollectionRuleResponseMetadata:
        
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
    @pulumi.getter(name="streamDeclarations")
    def stream_declarations(self) -> Optional[Mapping[str, outputs.StreamDeclarationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.DataCollectionRuleResourceResponseSystemData:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDataCollectionRuleResult(GetDataCollectionRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetDataCollectionRuleResult]:
        ...
    


def get_data_collection_rule(data_collection_rule_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataCollectionRuleResult:
    
    ...

def get_data_collection_rule_output(data_collection_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataCollectionRuleResult]:
    
    ...

