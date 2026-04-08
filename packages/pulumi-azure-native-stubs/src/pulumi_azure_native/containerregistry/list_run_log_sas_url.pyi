import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListRunLogSasUrlResult",
    "AwaitableListRunLogSasUrlResult",
    "list_run_log_sas_url",
    "list_run_log_sas_url_output",
]

@pulumi.output_type
class ListRunLogSasUrlResult:
    def __init__(__self__, log_artifact_link=..., log_link=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logArtifactLink")
    def log_artifact_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLink")
    def log_link(self) -> Optional[_builtins.str]: ...

class AwaitableListRunLogSasUrlResult(ListRunLogSasUrlResult):
    def __await__(self): ...

def list_run_log_sas_url(
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    run_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListRunLogSasUrlResult: ...
def list_run_log_sas_url_output(
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    run_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListRunLogSasUrlResult]: ...
