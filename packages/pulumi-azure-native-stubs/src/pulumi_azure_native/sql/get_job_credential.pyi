import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetJobCredentialResult",
    "AwaitableGetJobCredentialResult",
    "get_job_credential",
    "get_job_credential_output",
]

@pulumi.output_type
class GetJobCredentialResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., type=..., username=...
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
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

class AwaitableGetJobCredentialResult(GetJobCredentialResult):
    def __await__(self): ...

def get_job_credential(
    credential_name: Optional[_builtins.str] = ...,
    job_agent_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobCredentialResult: ...
def get_job_credential_output(
    credential_name: Optional[pulumi.Input[_builtins.str]] = ...,
    job_agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobCredentialResult]: ...
