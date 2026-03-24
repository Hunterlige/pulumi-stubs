import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDefaultKmsKeyResult",
    "AwaitableGetDefaultKmsKeyResult",
    "get_default_kms_key",
    "get_default_kms_key_output",
]

@pulumi.output_type
class GetDefaultKmsKeyResult:
    def __init__(__self__, id=..., key_arn=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDefaultKmsKeyResult(GetDefaultKmsKeyResult):
    def __await__(self): ...

def get_default_kms_key(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDefaultKmsKeyResult: ...
def get_default_kms_key_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDefaultKmsKeyResult]: ...
