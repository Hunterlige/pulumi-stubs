

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatascanIamPolicyResult', 'AwaitableGetDatascanIamPolicyResult', 'get_datascan_iam_policy', 'get_datascan_iam_policy_output']
@pulumi.output_type
class GetDatascanIamPolicyResult:
    
    def __init__(__self__, data_scan_id=..., etag=..., id=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataScanId")
    def data_scan_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetDatascanIamPolicyResult(GetDatascanIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetDatascanIamPolicyResult]:
        ...
    


def get_datascan_iam_policy(data_scan_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatascanIamPolicyResult:
    
    ...

def get_datascan_iam_policy_output(data_scan_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatascanIamPolicyResult]:
    
    ...

