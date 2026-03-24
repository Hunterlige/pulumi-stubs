

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListPolicySetDefinitionVersionAllBuiltinsResult', ..., 'list_policy_set_definition_version_all_builtins', ...]
@pulumi.output_type
class ListPolicySetDefinitionVersionAllBuiltinsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.PolicySetDefinitionVersionResponse]]:
        
        ...
    


class AwaitableListPolicySetDefinitionVersionAllBuiltinsResult(ListPolicySetDefinitionVersionAllBuiltinsResult):
    def __await__(self): # -> Generator[Never, Any, ListPolicySetDefinitionVersionAllBuiltinsResult]:
        ...
    


def list_policy_set_definition_version_all_builtins(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListPolicySetDefinitionVersionAllBuiltinsResult:
    
    ...

def list_policy_set_definition_version_all_builtins_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListPolicySetDefinitionVersionAllBuiltinsResult]:
    
    ...

