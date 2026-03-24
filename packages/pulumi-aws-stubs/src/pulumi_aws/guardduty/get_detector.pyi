

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDetectorResult', 'AwaitableGetDetectorResult', 'get_detector', 'get_detector_output']
@pulumi.output_type
class GetDetectorResult:
    
    def __init__(__self__, arn=..., features=..., finding_publishing_frequency=..., id=..., region=..., service_role_arn=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Sequence[outputs.GetDetectorFeatureResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetDetectorResult(GetDetectorResult):
    def __await__(self): # -> Generator[Never, Any, GetDetectorResult]:
        ...
    


def get_detector(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDetectorResult:
    
    ...

def get_detector_output(id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDetectorResult]:
    
    ...

