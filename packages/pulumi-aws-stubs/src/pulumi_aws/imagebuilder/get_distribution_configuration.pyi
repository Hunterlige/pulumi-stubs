

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDistributionConfigurationResult', 'AwaitableGetDistributionConfigurationResult', 'get_distribution_configuration', 'get_distribution_configuration_output']
@pulumi.output_type
class GetDistributionConfigurationResult:
    
    def __init__(__self__, arn=..., date_created=..., date_updated=..., description=..., distributions=..., id=..., name=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def distributions(self) -> Sequence[outputs.GetDistributionConfigurationDistributionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetDistributionConfigurationResult(GetDistributionConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetDistributionConfigurationResult]:
        ...
    


def get_distribution_configuration(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDistributionConfigurationResult:
    
    ...

def get_distribution_configuration_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDistributionConfigurationResult]:
    
    ...

