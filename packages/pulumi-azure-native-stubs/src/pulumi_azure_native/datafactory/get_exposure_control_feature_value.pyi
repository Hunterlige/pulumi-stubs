

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExposureControlFeatureValueResult', 'AwaitableGetExposureControlFeatureValueResult', 'get_exposure_control_feature_value', 'get_exposure_control_feature_value_output']
@pulumi.output_type
class GetExposureControlFeatureValueResult:
    
    def __init__(__self__, feature_name=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


class AwaitableGetExposureControlFeatureValueResult(GetExposureControlFeatureValueResult):
    def __await__(self): # -> Generator[Never, Any, GetExposureControlFeatureValueResult]:
        ...
    


def get_exposure_control_feature_value(feature_name: Optional[_builtins.str] = ..., feature_type: Optional[_builtins.str] = ..., location_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExposureControlFeatureValueResult:
    
    ...

def get_exposure_control_feature_value_output(feature_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., feature_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExposureControlFeatureValueResult]:
    
    ...

