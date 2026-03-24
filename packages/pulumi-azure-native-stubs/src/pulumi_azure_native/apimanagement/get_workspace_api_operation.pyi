

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceApiOperationResult', 'AwaitableGetWorkspaceApiOperationResult', 'get_workspace_api_operation', 'get_workspace_api_operation_output']
@pulumi.output_type
class GetWorkspaceApiOperationResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., method=..., name=..., policies=..., request=..., responses=..., template_parameters=..., type=..., url_template=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[outputs.RequestContractResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> Optional[Sequence[outputs.ResponseContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[Sequence[outputs.ParameterContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceApiOperationResult(GetWorkspaceApiOperationResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceApiOperationResult]:
        ...
    


def get_workspace_api_operation(api_id: Optional[_builtins.str] = ..., operation_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., workspace_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceApiOperationResult:
    
    ...

def get_workspace_api_operation_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., operation_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceApiOperationResult]:
    
    ...

