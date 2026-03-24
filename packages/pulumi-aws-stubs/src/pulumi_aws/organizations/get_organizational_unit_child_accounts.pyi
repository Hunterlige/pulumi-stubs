

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationalUnitChildAccountsResult', 'AwaitableGetOrganizationalUnitChildAccountsResult', 'get_organizational_unit_child_accounts', 'get_organizational_unit_child_accounts_output']
@pulumi.output_type
class GetOrganizationalUnitChildAccountsResult:
    
    def __init__(__self__, accounts=..., id=..., parent_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Sequence[outputs.GetOrganizationalUnitChildAccountsAccountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        ...
    


class AwaitableGetOrganizationalUnitChildAccountsResult(GetOrganizationalUnitChildAccountsResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationalUnitChildAccountsResult]:
        ...
    


def get_organizational_unit_child_accounts(parent_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationalUnitChildAccountsResult:
    
    ...

def get_organizational_unit_child_accounts_output(parent_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationalUnitChildAccountsResult]:
    
    ...

