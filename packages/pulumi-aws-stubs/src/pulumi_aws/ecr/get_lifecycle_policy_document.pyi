

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
__all__ = ['GetLifecyclePolicyDocumentResult', 'AwaitableGetLifecyclePolicyDocumentResult', 'get_lifecycle_policy_document', 'get_lifecycle_policy_document_output']
@pulumi.output_type
class GetLifecyclePolicyDocumentResult:
    
    def __init__(__self__, id=..., json=..., rules=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetLifecyclePolicyDocumentRuleResult]:
        ...
    


class AwaitableGetLifecyclePolicyDocumentResult(GetLifecyclePolicyDocumentResult):
    def __await__(self): # -> Generator[Never, Any, GetLifecyclePolicyDocumentResult]:
        ...
    


def get_lifecycle_policy_document(rules: Optional[Sequence[Union[GetLifecyclePolicyDocumentRuleArgs, GetLifecyclePolicyDocumentRuleArgsDict]]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLifecyclePolicyDocumentResult:
    
    ...

def get_lifecycle_policy_document_output(rules: Optional[pulumi.Input[Sequence[Union[GetLifecyclePolicyDocumentRuleArgs, GetLifecyclePolicyDocumentRuleArgsDict]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLifecyclePolicyDocumentResult]:
    
    ...

