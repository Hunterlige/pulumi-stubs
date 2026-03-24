

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GlobalSecondaryIndexArgs', 'GlobalSecondaryIndex']
@pulumi.input_type
class GlobalSecondaryIndexArgs:
    def __init__(__self__, *, index_name: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], key_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]] = ..., on_demand_throughput: Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]] = ..., projection: Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]] = ..., provisioned_throughput: Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]] = ..., warm_throughput: Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]]:
        
        ...
    
    @key_schemas.setter
    def key_schemas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]]:
        
        ...
    
    @on_demand_throughput.setter
    def on_demand_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def projection(self) -> Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]]:
        
        ...
    
    @projection.setter
    def projection(self, value: Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]]:
        
        ...
    
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]]:
        
        ...
    
    @warm_throughput.setter
    def warm_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _GlobalSecondaryIndexState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., key_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]] = ..., on_demand_throughput: Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]] = ..., projection: Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]] = ..., provisioned_throughput: Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]] = ..., warm_throughput: Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]]:
        
        ...
    
    @key_schemas.setter
    def key_schemas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalSecondaryIndexKeySchemaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]]:
        
        ...
    
    @on_demand_throughput.setter
    def on_demand_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexOnDemandThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def projection(self) -> Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]]:
        
        ...
    
    @projection.setter
    def projection(self, value: Optional[pulumi.Input[GlobalSecondaryIndexProjectionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]]:
        
        ...
    
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexProvisionedThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GlobalSecondaryIndexTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]]:
        
        ...
    
    @warm_throughput.setter
    def warm_throughput(self, value: Optional[pulumi.Input[GlobalSecondaryIndexWarmThroughputArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class GlobalSecondaryIndex(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., key_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GlobalSecondaryIndexKeySchemaArgs, GlobalSecondaryIndexKeySchemaArgsDict]]]]] = ..., on_demand_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexOnDemandThroughputArgs, GlobalSecondaryIndexOnDemandThroughputArgsDict]]] = ..., projection: Optional[pulumi.Input[Union[GlobalSecondaryIndexProjectionArgs, GlobalSecondaryIndexProjectionArgsDict]]] = ..., provisioned_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexProvisionedThroughputArgs, GlobalSecondaryIndexProvisionedThroughputArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[GlobalSecondaryIndexTimeoutsArgs, GlobalSecondaryIndexTimeoutsArgsDict]]] = ..., warm_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexWarmThroughputArgs, GlobalSecondaryIndexWarmThroughputArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GlobalSecondaryIndexArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., index_name: Optional[pulumi.Input[_builtins.str]] = ..., key_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GlobalSecondaryIndexKeySchemaArgs, GlobalSecondaryIndexKeySchemaArgsDict]]]]] = ..., on_demand_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexOnDemandThroughputArgs, GlobalSecondaryIndexOnDemandThroughputArgsDict]]] = ..., projection: Optional[pulumi.Input[Union[GlobalSecondaryIndexProjectionArgs, GlobalSecondaryIndexProjectionArgsDict]]] = ..., provisioned_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexProvisionedThroughputArgs, GlobalSecondaryIndexProvisionedThroughputArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[GlobalSecondaryIndexTimeoutsArgs, GlobalSecondaryIndexTimeoutsArgsDict]]] = ..., warm_throughput: Optional[pulumi.Input[Union[GlobalSecondaryIndexWarmThroughputArgs, GlobalSecondaryIndexWarmThroughputArgsDict]]] = ...) -> GlobalSecondaryIndex:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(self) -> pulumi.Output[Optional[Sequence[outputs.GlobalSecondaryIndexKeySchema]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> pulumi.Output[Optional[outputs.GlobalSecondaryIndexOnDemandThroughput]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def projection(self) -> pulumi.Output[Optional[outputs.GlobalSecondaryIndexProjection]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> pulumi.Output[Optional[outputs.GlobalSecondaryIndexProvisionedThroughput]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.GlobalSecondaryIndexTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> pulumi.Output[outputs.GlobalSecondaryIndexWarmThroughput]:
        
        ...
    


