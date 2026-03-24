

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetZoneIamPolicyResult', 'AwaitableGetZoneIamPolicyResult', 'get_zone_iam_policy', 'get_zone_iam_policy_output']
@pulumi.output_type
class GetZoneIamPolicyResult:
    
    def __init__(__self__, dataplex_zone=..., etag=..., id=..., lake=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> _builtins.str:
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
    def lake(self) -> _builtins.str:
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
    


class AwaitableGetZoneIamPolicyResult(GetZoneIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetZoneIamPolicyResult]:
        ...
    


def get_zone_iam_policy(dataplex_zone: Optional[_builtins.str] = ..., lake: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetZoneIamPolicyResult:
    
    ...

def get_zone_iam_policy_output(dataplex_zone: Optional[pulumi.Input[_builtins.str]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetZoneIamPolicyResult]:
    
    ...

