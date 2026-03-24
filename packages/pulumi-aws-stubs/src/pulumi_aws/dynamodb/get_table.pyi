

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTableResult', 'AwaitableGetTableResult', 'get_table', 'get_table_output']
@pulumi.output_type
class GetTableResult:
    
    def __init__(__self__, arn=..., attributes=..., billing_mode=..., deletion_protection_enabled=..., global_secondary_indexes=..., hash_key=..., id=..., local_secondary_indexes=..., name=..., on_demand_throughputs=..., point_in_time_recovery=..., range_key=..., read_capacity=..., region=..., replicas=..., server_side_encryption=..., stream_arn=..., stream_enabled=..., stream_label=..., stream_view_type=..., table_class=..., tags=..., ttl=..., warm_throughputs=..., write_capacity=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Sequence[outputs.GetTableAttributeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Sequence[outputs.GetTableGlobalSecondaryIndexResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Sequence[outputs.GetTableLocalSecondaryIndexResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughputs")
    def on_demand_throughputs(self) -> Sequence[outputs.GetTableOnDemandThroughputResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> outputs.GetTablePointInTimeRecoveryResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Sequence[outputs.GetTableReplicaResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> outputs.GetTableServerSideEncryptionResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamEnabled")
    def stream_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLabel")
    def stream_label(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> outputs.GetTableTtlResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughputs")
    def warm_throughputs(self) -> Sequence[outputs.GetTableWarmThroughputResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> _builtins.int:
        ...
    


class AwaitableGetTableResult(GetTableResult):
    def __await__(self): # -> Generator[Never, Any, GetTableResult]:
        ...
    


def get_table(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., server_side_encryption: Optional[Union[GetTableServerSideEncryptionArgs, GetTableServerSideEncryptionArgsDict]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTableResult:
    
    ...

def get_table_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., server_side_encryption: Optional[pulumi.Input[Optional[Union[GetTableServerSideEncryptionArgs, GetTableServerSideEncryptionArgsDict]]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTableResult]:
    
    ...

