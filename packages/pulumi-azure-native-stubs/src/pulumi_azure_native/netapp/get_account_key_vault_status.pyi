

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountKeyVaultStatusResult', 'AwaitableGetAccountKeyVaultStatusResult', 'get_account_key_vault_status', 'get_account_key_vault_status_output']
@pulumi.output_type
class GetAccountKeyVaultStatusResult:
    
    def __init__(__self__, key_name=..., key_vault_private_endpoints=..., key_vault_resource_id=..., key_vault_uri=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpoints")
    def key_vault_private_endpoints(self) -> Optional[Sequence[outputs.KeyVaultPrivateEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetAccountKeyVaultStatusResult(GetAccountKeyVaultStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountKeyVaultStatusResult]:
        ...
    


def get_account_key_vault_status(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountKeyVaultStatusResult:
    
    ...

def get_account_key_vault_status_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountKeyVaultStatusResult]:
    
    ...

