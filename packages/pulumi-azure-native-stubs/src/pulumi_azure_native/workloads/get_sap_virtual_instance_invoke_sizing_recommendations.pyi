

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetSapVirtualInstanceInvokeSizingRecommendationsResult:
    
    def __init__(__self__, deployment_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSapVirtualInstanceInvokeSizingRecommendationsResult(GetSapVirtualInstanceInvokeSizingRecommendationsResult):
    def __await__(self): # -> Generator[Never, Any, GetSapVirtualInstanceInvokeSizingRecommendationsResult]:
        ...
    


def get_sap_virtual_instance_invoke_sizing_recommendations(app_location: Optional[_builtins.str] = ..., database_type: Optional[Union[_builtins.str, SAPDatabaseType]] = ..., db_memory: Optional[_builtins.float] = ..., db_scale_method: Optional[Union[_builtins.str, SAPDatabaseScaleMethod]] = ..., deployment_type: Optional[Union[_builtins.str, SAPDeploymentType]] = ..., environment: Optional[Union[_builtins.str, SAPEnvironmentType]] = ..., high_availability_type: Optional[Union[_builtins.str, SAPHighAvailabilityType]] = ..., location: Optional[_builtins.str] = ..., sap_product: Optional[Union[_builtins.str, SAPProductType]] = ..., saps: Optional[_builtins.float] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapVirtualInstanceInvokeSizingRecommendationsResult:
    
    ...

def get_sap_virtual_instance_invoke_sizing_recommendations_output(app_location: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[Union[_builtins.str, SAPDatabaseType]]] = ..., db_memory: Optional[pulumi.Input[_builtins.float]] = ..., db_scale_method: Optional[pulumi.Input[Optional[Union[_builtins.str, SAPDatabaseScaleMethod]]]] = ..., deployment_type: Optional[pulumi.Input[Union[_builtins.str, SAPDeploymentType]]] = ..., environment: Optional[pulumi.Input[Union[_builtins.str, SAPEnvironmentType]]] = ..., high_availability_type: Optional[pulumi.Input[Optional[Union[_builtins.str, SAPHighAvailabilityType]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sap_product: Optional[pulumi.Input[Union[_builtins.str, SAPProductType]]] = ..., saps: Optional[pulumi.Input[_builtins.float]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapVirtualInstanceInvokeSizingRecommendationsResult]:
    
    ...

