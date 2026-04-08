import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDefenderForStorageResult",
    "AwaitableGetDefenderForStorageResult",
    "get_defender_for_storage",
    "get_defender_for_storage_output",
]

@pulumi.output_type
class GetDefenderForStorageResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.DefenderForStorageSettingPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDefenderForStorageResult(GetDefenderForStorageResult):
    def __await__(self): ...

def get_defender_for_storage(
    resource_id: Optional[_builtins.str] = ...,
    setting_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDefenderForStorageResult: ...
def get_defender_for_storage_output(
    resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDefenderForStorageResult]: ...
