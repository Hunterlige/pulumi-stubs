

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListSaasResourceAccessTokenResult', 'AwaitableListSaasResourceAccessTokenResult', 'list_saas_resource_access_token', 'list_saas_resource_access_token_output']
@pulumi.output_type
class ListSaasResourceAccessTokenResult:
    
    def __init__(__self__, publisher_offer_base_uri=..., token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherOfferBaseUri")
    def publisher_offer_base_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListSaasResourceAccessTokenResult(ListSaasResourceAccessTokenResult):
    def __await__(self): # -> Generator[Never, Any, ListSaasResourceAccessTokenResult]:
        ...
    


def list_saas_resource_access_token(resource_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSaasResourceAccessTokenResult:
    
    ...

def list_saas_resource_access_token_output(resource_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSaasResourceAccessTokenResult]:
    
    ...

