

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDocumentResult', 'AwaitableGetDocumentResult', 'get_document', 'get_document_output']
@pulumi.output_type
class GetDocumentResult:
    
    def __init__(__self__, collection=..., create_time=..., database=..., document_id=..., fields=..., id=..., name=..., path=..., project=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentId")
    def document_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetDocumentResult(GetDocumentResult):
    def __await__(self): # -> Generator[Never, Any, GetDocumentResult]:
        ...
    


def get_document(collection: Optional[_builtins.str] = ..., database: Optional[_builtins.str] = ..., document_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDocumentResult:
    
    ...

def get_document_output(collection: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., document_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDocumentResult]:
    
    ...

