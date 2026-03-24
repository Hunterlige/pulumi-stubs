

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPythonPackagesResult', 'AwaitableGetPythonPackagesResult', 'get_python_packages', 'get_python_packages_output']
@pulumi.output_type
class GetPythonPackagesResult:
    
    def __init__(__self__, id=..., location=..., project=..., python_packages=..., repository_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(self) -> Sequence[outputs.GetPythonPackagesPythonPackageResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        ...
    


class AwaitableGetPythonPackagesResult(GetPythonPackagesResult):
    def __await__(self): # -> Generator[Never, Any, GetPythonPackagesResult]:
        ...
    


def get_python_packages(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPythonPackagesResult:
    
    ...

def get_python_packages_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPythonPackagesResult]:
    
    ...

