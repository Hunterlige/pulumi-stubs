

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOdbSubnetResult', 'AwaitableGetOdbSubnetResult', 'get_odb_subnet', 'get_odb_subnet_output']
@pulumi.output_type
class GetOdbSubnetResult:
    
    def __init__(__self__, cidr_range=..., create_time=..., deletion_protection=..., effective_labels=..., id=..., labels=..., location=..., name=..., odb_subnet_id=..., odbnetwork=..., project=..., pulumi_labels=..., purpose=..., state=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrRange")
    def cidr_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbSubnetId")
    def odb_subnet_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def odbnetwork(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


class AwaitableGetOdbSubnetResult(GetOdbSubnetResult):
    def __await__(self): # -> Generator[Never, Any, GetOdbSubnetResult]:
        ...
    


def get_odb_subnet(location: Optional[_builtins.str] = ..., odb_subnet_id: Optional[_builtins.str] = ..., odbnetwork: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOdbSubnetResult:
    
    ...

def get_odb_subnet_output(location: Optional[pulumi.Input[_builtins.str]] = ..., odb_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., odbnetwork: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOdbSubnetResult]:
    
    ...

