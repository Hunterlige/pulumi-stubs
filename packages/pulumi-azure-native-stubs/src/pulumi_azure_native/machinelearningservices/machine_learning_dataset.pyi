

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MachineLearningDatasetArgs', 'MachineLearningDataset']
@pulumi.input_type
class MachineLearningDatasetArgs:
    def __init__(__self__, *, dataset_type: pulumi.Input[Union[_builtins.str, DatasetType]], parameters: pulumi.Input[DatasetCreateRequestParametersArgs], registration: pulumi.Input[DatasetCreateRequestRegistrationArgs], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], dataset_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_validation: Optional[pulumi.Input[_builtins.bool]] = ..., time_series: Optional[pulumi.Input[DatasetCreateRequestTimeSeriesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetType")
    def dataset_type(self) -> pulumi.Input[Union[_builtins.str, DatasetType]]:
        
        ...
    
    @dataset_type.setter
    def dataset_type(self, value: pulumi.Input[Union[_builtins.str, DatasetType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[DatasetCreateRequestParametersArgs]:
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[DatasetCreateRequestParametersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> pulumi.Input[DatasetCreateRequestRegistrationArgs]:
        ...
    
    @registration.setter
    def registration(self, value: pulumi.Input[DatasetCreateRequestRegistrationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetName")
    def dataset_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_name.setter
    def dataset_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> Optional[pulumi.Input[DatasetCreateRequestTimeSeriesArgs]]:
        ...
    
    @time_series.setter
    def time_series(self, value: Optional[pulumi.Input[DatasetCreateRequestTimeSeriesArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MachineLearningDataset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dataset_name: Optional[pulumi.Input[_builtins.str]] = ..., dataset_type: Optional[pulumi.Input[Union[_builtins.str, DatasetType]]] = ..., parameters: Optional[pulumi.Input[Union[DatasetCreateRequestParametersArgs, DatasetCreateRequestParametersArgsDict]]] = ..., registration: Optional[pulumi.Input[Union[DatasetCreateRequestRegistrationArgs, DatasetCreateRequestRegistrationArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_validation: Optional[pulumi.Input[_builtins.bool]] = ..., time_series: Optional[pulumi.Input[Union[DatasetCreateRequestTimeSeriesArgs, DatasetCreateRequestTimeSeriesArgsDict]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MachineLearningDatasetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MachineLearningDataset:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponseV1]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.DatasetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponseV1]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


