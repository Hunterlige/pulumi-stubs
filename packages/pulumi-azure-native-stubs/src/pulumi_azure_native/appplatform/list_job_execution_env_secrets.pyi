import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListJobExecutionEnvSecretsResult",
    "AwaitableListJobExecutionEnvSecretsResult",
    "list_job_execution_env_secrets",
    "list_job_execution_env_secrets_output",
]

@pulumi.output_type
class ListJobExecutionEnvSecretsResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.SecretResponse]: ...

class AwaitableListJobExecutionEnvSecretsResult(ListJobExecutionEnvSecretsResult):
    def __await__(self): ...

def list_job_execution_env_secrets(
    job_execution_name: Optional[_builtins.str] = ...,
    job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListJobExecutionEnvSecretsResult: ...
def list_job_execution_env_secrets_output(
    job_execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
    job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListJobExecutionEnvSecretsResult]: ...
