

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
__all__ = ['LinkedDatasetArgs', 'LinkedDataset']
@pulumi.input_type
class LinkedDatasetArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], link_id: pulumi.Input[_builtins.str], bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @link_id.setter
    def link_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]]:
        
        ...
    
    @bigquery_datasets.setter
    def bigquery_datasets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LinkedDatasetState:
    def __init__(__self__, *, bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]]:
        
        ...
    
    @bigquery_datasets.setter
    def bigquery_datasets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedDatasetBigqueryDatasetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:logging/linkedDataset:LinkedDataset")
class LinkedDataset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LinkedDatasetBigqueryDatasetArgs, LinkedDatasetBigqueryDatasetArgsDict]]]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LinkedDatasetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LinkedDatasetBigqueryDatasetArgs, LinkedDatasetBigqueryDatasetArgsDict]]]]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> LinkedDataset:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> pulumi.Output[Sequence[outputs.LinkedDatasetBigqueryDataset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


