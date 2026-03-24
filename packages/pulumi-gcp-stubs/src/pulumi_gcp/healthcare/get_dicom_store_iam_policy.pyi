

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDicomStoreIamPolicyResult', 'AwaitableGetDicomStoreIamPolicyResult', 'get_dicom_store_iam_policy', 'get_dicom_store_iam_policy_output']
@pulumi.output_type
class GetDicomStoreIamPolicyResult:
    
    def __init__(__self__, dicom_store_id=..., etag=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> _builtins.str:
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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDicomStoreIamPolicyResult(GetDicomStoreIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetDicomStoreIamPolicyResult]:
        ...
    


def get_dicom_store_iam_policy(dicom_store_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDicomStoreIamPolicyResult:
    
    ...

def get_dicom_store_iam_policy_output(dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDicomStoreIamPolicyResult]:
    
    ...

