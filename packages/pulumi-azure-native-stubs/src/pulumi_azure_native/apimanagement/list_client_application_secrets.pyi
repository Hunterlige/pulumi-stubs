

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListClientApplicationSecretsResult', 'AwaitableListClientApplicationSecretsResult', 'list_client_application_secrets', 'list_client_application_secrets_output']
@pulumi.output_type
class ListClientApplicationSecretsResult:
    
    def __init__(__self__, entra=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entra(self) -> Optional[outputs.ClientApplicationSecretsContractResponseEntra]:
        
        ...
    


class AwaitableListClientApplicationSecretsResult(ListClientApplicationSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListClientApplicationSecretsResult]:
        ...
    


def list_client_application_secrets(client_application_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListClientApplicationSecretsResult:
    
    ...

def list_client_application_secrets_output(client_application_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListClientApplicationSecretsResult]:
    
    ...

