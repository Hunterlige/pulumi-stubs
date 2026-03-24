

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExposureControlFeatureValueByFactoryResult', ..., 'get_exposure_control_feature_value_by_factory', ...]
@pulumi.output_type
class GetExposureControlFeatureValueByFactoryResult:
    
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
    


class AwaitableGetExposureControlFeatureValueByFactoryResult(GetExposureControlFeatureValueByFactoryResult):
    def __await__(self): # -> Generator[Never, Any, GetExposureControlFeatureValueByFactoryResult]:
        ...
    


def get_exposure_control_feature_value_by_factory(factory_name: Optional[_builtins.str] = ..., feature_name: Optional[_builtins.str] = ..., feature_type: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExposureControlFeatureValueByFactoryResult:
    
    ...

def get_exposure_control_feature_value_by_factory_output(factory_name: Optional[pulumi.Input[_builtins.str]] = ..., feature_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., feature_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExposureControlFeatureValueByFactoryResult]:
    
    ...

