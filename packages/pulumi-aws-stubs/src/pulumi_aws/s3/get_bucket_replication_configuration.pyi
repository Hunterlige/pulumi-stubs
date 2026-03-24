import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBucketReplicationConfigurationResult",
    "AwaitableGetBucketReplicationConfigurationResult",
    "get_bucket_replication_configuration",
    "get_bucket_replication_configuration_output",
]

@pulumi.output_type
class GetBucketReplicationConfigurationResult:
    def __init__(
        __self__, bucket=..., id=..., region=..., role=..., rules=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleResult]: ...

class AwaitableGetBucketReplicationConfigurationResult(
    GetBucketReplicationConfigurationResult
):
    def __await__(self): ...

def get_bucket_replication_configuration(
    bucket: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBucketReplicationConfigurationResult: ...
def get_bucket_replication_configuration_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBucketReplicationConfigurationResult]: ...
