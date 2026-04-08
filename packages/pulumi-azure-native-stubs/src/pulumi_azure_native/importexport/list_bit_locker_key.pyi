import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListBitLockerKeyResult",
    "AwaitableListBitLockerKeyResult",
    "list_bit_locker_key",
    "list_bit_locker_key_output",
]

@pulumi.output_type
class ListBitLockerKeyResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.DriveBitLockerKeyResponse]]: ...

class AwaitableListBitLockerKeyResult(ListBitLockerKeyResult):
    def __await__(self): ...

def list_bit_locker_key(
    job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListBitLockerKeyResult: ...
def list_bit_locker_key_output(
    job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListBitLockerKeyResult]: ...
