

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetComponentCurrentBillingFeatureResult', 'AwaitableGetComponentCurrentBillingFeatureResult', 'get_component_current_billing_feature', 'get_component_current_billing_feature_output']
@pulumi.output_type
class GetComponentCurrentBillingFeatureResult:
    
    def __init__(__self__, azure_api_version=..., current_billing_features=..., data_volume_cap=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentBillingFeatures")
    def current_billing_features(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataVolumeCap")
    def data_volume_cap(self) -> Optional[outputs.ApplicationInsightsComponentDataVolumeCapResponse]:
        
        ...
    


class AwaitableGetComponentCurrentBillingFeatureResult(GetComponentCurrentBillingFeatureResult):
    def __await__(self): # -> Generator[Never, Any, GetComponentCurrentBillingFeatureResult]:
        ...
    


def get_component_current_billing_feature(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetComponentCurrentBillingFeatureResult:
    
    ...

def get_component_current_billing_feature_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetComponentCurrentBillingFeatureResult]:
    
    ...

