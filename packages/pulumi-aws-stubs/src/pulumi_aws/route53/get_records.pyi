import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRecordsResult",
    "AwaitableGetRecordsResult",
    "get_records",
    "get_records_output",
]

@pulumi.output_type
class GetRecordsResult:
    def __init__(
        __self__, id=..., name_regex=..., resource_record_sets=..., zone_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRecordSets")
    def resource_record_sets(
        self,
    ) -> Sequence[outputs.GetRecordsResourceRecordSetResult]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str: ...

class AwaitableGetRecordsResult(GetRecordsResult):
    def __await__(self): ...

def get_records(
    name_regex: Optional[_builtins.str] = ...,
    zone_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRecordsResult: ...
def get_records_output(
    name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRecordsResult]: ...
