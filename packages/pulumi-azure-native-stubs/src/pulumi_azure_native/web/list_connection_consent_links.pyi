

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListConnectionConsentLinksResult', 'AwaitableListConnectionConsentLinksResult', 'list_connection_consent_links', 'list_connection_consent_links_output']
@pulumi.output_type
class ListConnectionConsentLinksResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ConsentLinkDefinitionResponse]]:
        
        ...
    


class AwaitableListConnectionConsentLinksResult(ListConnectionConsentLinksResult):
    def __await__(self): # -> Generator[Never, Any, ListConnectionConsentLinksResult]:
        ...
    


def list_connection_consent_links(connection_name: Optional[_builtins.str] = ..., parameters: Optional[Sequence[Union[ConsentLinkParameterDefinition, ConsentLinkParameterDefinitionDict]]] = ..., resource_group_name: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListConnectionConsentLinksResult:
    
    ...

def list_connection_consent_links_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Optional[Sequence[Union[ConsentLinkParameterDefinition, ConsentLinkParameterDefinitionDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListConnectionConsentLinksResult]:
    
    ...

