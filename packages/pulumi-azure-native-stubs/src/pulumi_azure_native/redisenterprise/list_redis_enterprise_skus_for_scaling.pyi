import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListRedisEnterpriseSkusForScalingResult",
    "AwaitableListRedisEnterpriseSkusForScalingResult",
    "list_redis_enterprise_skus_for_scaling",
    "list_redis_enterprise_skus_for_scaling_output",
]

@pulumi.output_type
class ListRedisEnterpriseSkusForScalingResult:
    def __init__(__self__, skus=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def skus(self) -> Optional[Sequence[outputs.SkuDetailsResponse]]: ...

class AwaitableListRedisEnterpriseSkusForScalingResult(
    ListRedisEnterpriseSkusForScalingResult
):
    def __await__(self): ...

def list_redis_enterprise_skus_for_scaling(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListRedisEnterpriseSkusForScalingResult: ...
def list_redis_enterprise_skus_for_scaling_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListRedisEnterpriseSkusForScalingResult]: ...
