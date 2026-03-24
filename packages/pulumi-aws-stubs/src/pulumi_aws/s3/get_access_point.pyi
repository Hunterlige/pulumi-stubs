

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccessPointResult', 'AwaitableGetAccessPointResult', 'get_access_point', 'get_access_point_output']
@pulumi.output_type
class GetAccessPointResult:
    
    def __init__(__self__, account_id=..., alias=..., arn=..., bucket=..., bucket_account_id=..., data_source_id=..., data_source_type=..., endpoints=..., id=..., name=..., network_origin=..., public_access_block_configurations=..., region=..., tags=..., vpc_configurations=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Mapping[str, _builtins.str]:
        
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
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessBlockConfigurations")
    def public_access_block_configurations(self) -> Sequence[outputs.GetAccessPointPublicAccessBlockConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfigurations")
    def vpc_configurations(self) -> Sequence[outputs.GetAccessPointVpcConfigurationResult]:
        
        ...
    


class AwaitableGetAccessPointResult(GetAccessPointResult):
    def __await__(self): # -> Generator[Never, Any, GetAccessPointResult]:
        ...
    


def get_access_point(account_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccessPointResult:
    
    ...

def get_access_point_output(account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccessPointResult]:
    
    ...

