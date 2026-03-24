

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationApiKeyResult', 'AwaitableGetOrganizationApiKeyResult', 'get_organization_api_key', 'get_organization_api_key_output']
@pulumi.output_type
class GetOrganizationApiKeyResult:
    
    def __init__(__self__, properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.UserApiKeyResponsePropertiesResponse:
        ...
    


class AwaitableGetOrganizationApiKeyResult(GetOrganizationApiKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationApiKeyResult]:
        ...
    


def get_organization_api_key(email_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationApiKeyResult:
    
    ...

def get_organization_api_key_output(email_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationApiKeyResult]:
    
    ...

