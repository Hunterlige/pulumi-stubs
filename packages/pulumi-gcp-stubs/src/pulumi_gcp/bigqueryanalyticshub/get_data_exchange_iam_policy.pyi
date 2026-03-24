

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataExchangeIamPolicyResult', 'AwaitableGetDataExchangeIamPolicyResult', 'get_data_exchange_iam_policy', 'get_data_exchange_iam_policy_output']
@pulumi.output_type
class GetDataExchangeIamPolicyResult:
    
    def __init__(__self__, data_exchange_id=..., etag=..., id=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> _builtins.str:
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
    


class AwaitableGetDataExchangeIamPolicyResult(GetDataExchangeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetDataExchangeIamPolicyResult]:
        ...
    


def get_data_exchange_iam_policy(data_exchange_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataExchangeIamPolicyResult:
    
    ...

def get_data_exchange_iam_policy_output(data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataExchangeIamPolicyResult]:
    
    ...

