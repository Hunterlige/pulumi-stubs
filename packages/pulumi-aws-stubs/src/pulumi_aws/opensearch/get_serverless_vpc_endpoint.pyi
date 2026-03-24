

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessVpcEndpointResult', 'AwaitableGetServerlessVpcEndpointResult', 'get_serverless_vpc_endpoint', 'get_serverless_vpc_endpoint_output']
@pulumi.output_type
class GetServerlessVpcEndpointResult:
    
    def __init__(__self__, created_date=..., id=..., name=..., region=..., security_group_ids=..., subnet_ids=..., vpc_endpoint_id=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
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
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerlessVpcEndpointResult(GetServerlessVpcEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessVpcEndpointResult]:
        ...
    


def get_serverless_vpc_endpoint(region: Optional[_builtins.str] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessVpcEndpointResult:
    
    ...

def get_serverless_vpc_endpoint_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessVpcEndpointResult]:
    
    ...

