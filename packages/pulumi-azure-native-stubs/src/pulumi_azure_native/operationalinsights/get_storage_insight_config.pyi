import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStorageInsightConfigResult",
    "AwaitableGetStorageInsightConfigResult",
    "get_storage_insight_config",
    "get_storage_insight_config_output",
]

@pulumi.output_type
class GetStorageInsightConfigResult:
    def __init__(
        __self__,
        azure_api_version=...,
        containers=...,
        e_tag=...,
        id=...,
        name=...,
        status=...,
        storage_account=...,
        tables=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.StorageInsightStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> outputs.StorageAccountResponse: ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStorageInsightConfigResult(GetStorageInsightConfigResult):
    def __await__(self): ...

def get_storage_insight_config(
    resource_group_name: Optional[_builtins.str] = ...,
    storage_insight_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStorageInsightConfigResult: ...
def get_storage_insight_config_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    storage_insight_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStorageInsightConfigResult]: ...
