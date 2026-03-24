

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSQuotaInfosResult', 'AwaitableGetSQuotaInfosResult', 'get_s_quota_infos', 'get_s_quota_infos_output']
@pulumi.output_type
class GetSQuotaInfosResult:
    
    def __init__(__self__, id=..., parent=..., quota_infos=..., service=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaInfos")
    def quota_infos(self) -> Sequence[outputs.GetSQuotaInfosQuotaInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        ...
    


class AwaitableGetSQuotaInfosResult(GetSQuotaInfosResult):
    def __await__(self): # -> Generator[Never, Any, GetSQuotaInfosResult]:
        ...
    


def get_s_quota_infos(parent: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSQuotaInfosResult:
    
    ...

def get_s_quota_infos_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSQuotaInfosResult]:
    
    ...

