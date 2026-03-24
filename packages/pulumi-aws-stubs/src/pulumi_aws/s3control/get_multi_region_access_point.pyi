import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMultiRegionAccessPointResult",
    "AwaitableGetMultiRegionAccessPointResult",
    "get_multi_region_access_point",
    "get_multi_region_access_point_output",
]

@pulumi.output_type
class GetMultiRegionAccessPointResult:
    def __init__(
        __self__,
        account_id=...,
        alias=...,
        arn=...,
        created_at=...,
        domain_name=...,
        id=...,
        name=...,
        public_access_blocks=...,
        region=...,
        regions=...,
        status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlocks")
    def public_access_blocks(
        self,
    ) -> Sequence[outputs.GetMultiRegionAccessPointPublicAccessBlockResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[outputs.GetMultiRegionAccessPointRegionResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

class AwaitableGetMultiRegionAccessPointResult(GetMultiRegionAccessPointResult):
    def __await__(self): ...

def get_multi_region_access_point(
    account_id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMultiRegionAccessPointResult: ...
def get_multi_region_access_point_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMultiRegionAccessPointResult]: ...
