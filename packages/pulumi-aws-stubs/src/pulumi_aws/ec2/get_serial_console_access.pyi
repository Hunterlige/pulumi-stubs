import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSerialConsoleAccessResult",
    "AwaitableGetSerialConsoleAccessResult",
    "get_serial_console_access",
    "get_serial_console_access_output",
]

@pulumi.output_type
class GetSerialConsoleAccessResult:
    def __init__(__self__, enabled=..., id=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetSerialConsoleAccessResult(GetSerialConsoleAccessResult):
    def __await__(self): ...

def get_serial_console_access(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetSerialConsoleAccessResult: ...
def get_serial_console_access_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSerialConsoleAccessResult]: ...
