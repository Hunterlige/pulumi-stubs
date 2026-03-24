

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiIndexResult', 'AwaitableGetAiIndexResult', 'get_ai_index', 'get_ai_index_output']
@pulumi.output_type
class GetAiIndexResult:
    
    def __init__(__self__, create_time=..., deployed_indexes=..., description=..., display_name=..., effective_labels=..., encryption_specs=..., etag=..., id=..., index_stats=..., index_update_method=..., labels=..., metadata_schema_uri=..., metadatas=..., name=..., project=..., pulumi_labels=..., region=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexes")
    def deployed_indexes(self) -> Sequence[outputs.GetAiIndexDeployedIndexResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSpecs")
    def encryption_specs(self) -> Sequence[outputs.GetAiIndexEncryptionSpecResult]:
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
    @pulumi.getter(name="indexStats")
    def index_stats(self) -> Sequence[outputs.GetAiIndexIndexStatResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexUpdateMethod")
    def index_update_method(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataSchemaUri")
    def metadata_schema_uri(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> Sequence[outputs.GetAiIndexMetadataResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetAiIndexResult(GetAiIndexResult):
    def __await__(self): # -> Generator[Never, Any, GetAiIndexResult]:
        ...
    


def get_ai_index(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiIndexResult:
    
    ...

def get_ai_index_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiIndexResult]:
    
    ...

