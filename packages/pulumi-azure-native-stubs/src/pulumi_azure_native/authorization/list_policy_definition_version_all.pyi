import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListPolicyDefinitionVersionAllResult",
    "AwaitableListPolicyDefinitionVersionAllResult",
    "list_policy_definition_version_all",
    "list_policy_definition_version_all_output",
]

@pulumi.output_type
class ListPolicyDefinitionVersionAllResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.PolicyDefinitionVersionResponse]]: ...

class AwaitableListPolicyDefinitionVersionAllResult(
    ListPolicyDefinitionVersionAllResult
):
    def __await__(self): ...

def list_policy_definition_version_all(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPolicyDefinitionVersionAllResult: ...
def list_policy_definition_version_all_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListPolicyDefinitionVersionAllResult]: ...
