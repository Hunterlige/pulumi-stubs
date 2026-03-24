

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListBuildServiceBuilderDeploymentsResult', 'AwaitableListBuildServiceBuilderDeploymentsResult', 'list_build_service_builder_deployments', 'list_build_service_builder_deployments_output']
@pulumi.output_type
class ListBuildServiceBuilderDeploymentsResult:
    
    def __init__(__self__, deployments=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployments(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableListBuildServiceBuilderDeploymentsResult(ListBuildServiceBuilderDeploymentsResult):
    def __await__(self): # -> Generator[Never, Any, ListBuildServiceBuilderDeploymentsResult]:
        ...
    


def list_build_service_builder_deployments(build_service_name: Optional[_builtins.str] = ..., builder_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListBuildServiceBuilderDeploymentsResult:
    
    ...

def list_build_service_builder_deployments_output(build_service_name: Optional[pulumi.Input[_builtins.str]] = ..., builder_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListBuildServiceBuilderDeploymentsResult]:
    
    ...

