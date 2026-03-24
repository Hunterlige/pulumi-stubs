

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyDocumentResult', 'AwaitableGetPolicyDocumentResult', 'get_policy_document', 'get_policy_document_output']
@pulumi.output_type
class GetPolicyDocumentResult:
    
    def __init__(__self__, id=..., json=..., minified_json=..., override_json=..., override_policy_documents=..., policy_id=..., source_json=..., source_policy_documents=..., statements=..., version=...) -> None:
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
    @pulumi.getter(name="minifiedJson")
    def minified_json(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideJson")
    @_utilities.deprecated(...)
    def override_json(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overridePolicyDocuments")
    def override_policy_documents(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceJson")
    @_utilities.deprecated(...)
    def source_json(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePolicyDocuments")
    def source_policy_documents(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Optional[Sequence[outputs.GetPolicyDocumentStatementResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetPolicyDocumentResult(GetPolicyDocumentResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyDocumentResult]:
        ...
    


def get_policy_document(override_json: Optional[_builtins.str] = ..., override_policy_documents: Optional[Sequence[_builtins.str]] = ..., policy_id: Optional[_builtins.str] = ..., source_json: Optional[_builtins.str] = ..., source_policy_documents: Optional[Sequence[_builtins.str]] = ..., statements: Optional[Sequence[Union[GetPolicyDocumentStatementArgs, GetPolicyDocumentStatementArgsDict]]] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyDocumentResult:
    
    ...

def get_policy_document_output(override_json: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., override_policy_documents: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., policy_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., source_json: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., source_policy_documents: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., statements: Optional[pulumi.Input[Optional[Sequence[Union[GetPolicyDocumentStatementArgs, GetPolicyDocumentStatementArgsDict]]]]] = ..., version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyDocumentResult]:
    
    ...

