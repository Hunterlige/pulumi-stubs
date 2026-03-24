

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFileShareProvisioningRecommendationResult', ..., 'get_file_share_provisioning_recommendation', 'get_file_share_provisioning_recommendation_output']
@pulumi.output_type
class GetFileShareProvisioningRecommendationResult:
    
    def __init__(__self__, properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.FileShareProvisioningRecommendationOutputResponse:
        
        ...
    


class AwaitableGetFileShareProvisioningRecommendationResult(GetFileShareProvisioningRecommendationResult):
    def __await__(self): # -> Generator[Never, Any, GetFileShareProvisioningRecommendationResult]:
        ...
    


def get_file_share_provisioning_recommendation(location: Optional[_builtins.str] = ..., properties: Optional[Union[FileShareProvisioningRecommendationInput, FileShareProvisioningRecommendationInputDict]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFileShareProvisioningRecommendationResult:
    
    ...

def get_file_share_provisioning_recommendation_output(location: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[FileShareProvisioningRecommendationInput, FileShareProvisioningRecommendationInputDict]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFileShareProvisioningRecommendationResult]:
    
    ...

