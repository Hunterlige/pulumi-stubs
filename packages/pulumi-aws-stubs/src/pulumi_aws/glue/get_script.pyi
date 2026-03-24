

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
__all__ = ['GetScriptResult', 'AwaitableGetScriptResult', 'get_script', 'get_script_output']
@pulumi.output_type
class GetScriptResult:
    
    def __init__(__self__, dag_edges=..., dag_nodes=..., id=..., language=..., python_script=..., region=..., scala_code=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagEdges")
    def dag_edges(self) -> Sequence[outputs.GetScriptDagEdgeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagNodes")
    def dag_nodes(self) -> Sequence[outputs.GetScriptDagNodeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonScript")
    def python_script(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalaCode")
    def scala_code(self) -> _builtins.str:
        
        ...
    


class AwaitableGetScriptResult(GetScriptResult):
    def __await__(self): # -> Generator[Never, Any, GetScriptResult]:
        ...
    


def get_script(dag_edges: Optional[Sequence[Union[GetScriptDagEdgeArgs, GetScriptDagEdgeArgsDict]]] = ..., dag_nodes: Optional[Sequence[Union[GetScriptDagNodeArgs, GetScriptDagNodeArgsDict]]] = ..., language: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScriptResult:
    
    ...

def get_script_output(dag_edges: Optional[pulumi.Input[Sequence[Union[GetScriptDagEdgeArgs, GetScriptDagEdgeArgsDict]]]] = ..., dag_nodes: Optional[pulumi.Input[Sequence[Union[GetScriptDagNodeArgs, GetScriptDagNodeArgsDict]]]] = ..., language: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScriptResult]:
    
    ...

