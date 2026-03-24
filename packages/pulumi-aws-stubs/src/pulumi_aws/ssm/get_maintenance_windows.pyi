import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMaintenanceWindowsResult",
    "AwaitableGetMaintenanceWindowsResult",
    "get_maintenance_windows",
    "get_maintenance_windows_output",
]

@pulumi.output_type
class GetMaintenanceWindowsResult:
    def __init__(__self__, filters=..., id=..., ids=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetMaintenanceWindowsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetMaintenanceWindowsResult(GetMaintenanceWindowsResult):
    def __await__(self): ...

def get_maintenance_windows(
    filters: Optional[
        Sequence[
            Union[GetMaintenanceWindowsFilterArgs, GetMaintenanceWindowsFilterArgsDict]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMaintenanceWindowsResult: ...
def get_maintenance_windows_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetMaintenanceWindowsFilterArgs,
                        GetMaintenanceWindowsFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMaintenanceWindowsResult]: ...
