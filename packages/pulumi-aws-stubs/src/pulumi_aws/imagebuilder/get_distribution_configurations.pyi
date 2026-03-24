

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDistributionConfigurationsResult', 'AwaitableGetDistributionConfigurationsResult', 'get_distribution_configurations', 'get_distribution_configurations_output']
@pulumi.output_type
class GetDistributionConfigurationsResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., names=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetDistributionConfigurationsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetDistributionConfigurationsResult(GetDistributionConfigurationsResult):
    def __await__(self): # -> Generator[Never, Any, GetDistributionConfigurationsResult]:
        ...
    


def get_distribution_configurations(filters: Optional[Sequence[Union[GetDistributionConfigurationsFilterArgs, GetDistributionConfigurationsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDistributionConfigurationsResult:
    
    ...

def get_distribution_configurations_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetDistributionConfigurationsFilterArgs, GetDistributionConfigurationsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDistributionConfigurationsResult]:
    
    ...

