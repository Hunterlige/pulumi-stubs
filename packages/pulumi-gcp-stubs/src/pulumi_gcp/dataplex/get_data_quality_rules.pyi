

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataQualityRulesResult', 'AwaitableGetDataQualityRulesResult', 'get_data_quality_rules', 'get_data_quality_rules_output']
@pulumi.output_type
class GetDataQualityRulesResult:
    
    def __init__(__self__, data_scan_id=..., id=..., location=..., project=..., rules=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataScanId")
    def data_scan_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetDataQualityRulesRuleResult]:
        
        ...
    


class AwaitableGetDataQualityRulesResult(GetDataQualityRulesResult):
    def __await__(self): # -> Generator[Never, Any, GetDataQualityRulesResult]:
        ...
    


def get_data_quality_rules(data_scan_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataQualityRulesResult:
    
    ...

def get_data_quality_rules_output(data_scan_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataQualityRulesResult]:
    
    ...

