

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPredictionModelStatusResult', 'AwaitableGetPredictionModelStatusResult', 'get_prediction_model_status', 'get_prediction_model_status_output']
@pulumi.output_type
class GetPredictionModelStatusResult:
    
    def __init__(__self__, message=..., model_version=..., prediction_guid_id=..., prediction_name=..., signals_used=..., status=..., tenant_id=..., test_set_count=..., training_accuracy=..., training_set_count=..., validation_set_count=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictionGuidId")
    def prediction_guid_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signalsUsed")
    def signals_used(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testSetCount")
    def test_set_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trainingAccuracy")
    def training_accuracy(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trainingSetCount")
    def training_set_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationSetCount")
    def validation_set_count(self) -> _builtins.int:
        
        ...
    


class AwaitableGetPredictionModelStatusResult(GetPredictionModelStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetPredictionModelStatusResult]:
        ...
    


def get_prediction_model_status(hub_name: Optional[_builtins.str] = ..., prediction_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPredictionModelStatusResult:
    
    ...

def get_prediction_model_status_output(hub_name: Optional[pulumi.Input[_builtins.str]] = ..., prediction_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPredictionModelStatusResult]:
    
    ...

