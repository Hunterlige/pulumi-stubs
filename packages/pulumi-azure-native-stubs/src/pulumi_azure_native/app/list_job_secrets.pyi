

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListJobSecretsResult', 'AwaitableListJobSecretsResult', 'list_job_secrets', 'list_job_secrets_output']
@pulumi.output_type
class ListJobSecretsResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.SecretResponse]:
        
        ...
    


class AwaitableListJobSecretsResult(ListJobSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListJobSecretsResult]:
        ...
    


def list_job_secrets(job_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListJobSecretsResult:
    
    ...

def list_job_secrets_output(job_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListJobSecretsResult]:
    
    ...

