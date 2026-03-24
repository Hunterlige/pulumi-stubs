

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetListingIamPolicyResult', 'AwaitableGetListingIamPolicyResult', 'get_listing_iam_policy', 'get_listing_iam_policy_output']
@pulumi.output_type
class GetListingIamPolicyResult:
    
    def __init__(__self__, data_exchange_id=..., etag=..., id=..., listing_id=..., location=..., policy_data=..., project=...) -> None:
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
    @pulumi.getter(name="listingId")
    def listing_id(self) -> _builtins.str:
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
    


class AwaitableGetListingIamPolicyResult(GetListingIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetListingIamPolicyResult]:
        ...
    


def get_listing_iam_policy(data_exchange_id: Optional[_builtins.str] = ..., listing_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetListingIamPolicyResult:
    
    ...

def get_listing_iam_policy_output(data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., listing_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetListingIamPolicyResult]:
    
    ...

