

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPipelineResult', 'AwaitableGetPipelineResult', 'get_pipeline', 'get_pipeline_output']
@pulumi.output_type
class GetPipelineResult:
    
    def __init__(__self__, activities=..., annotations=..., azure_api_version=..., concurrency=..., description=..., etag=..., folder=..., id=..., name=..., parameters=..., policy=..., run_dimensions=..., type=..., variables=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def activities(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[outputs.PipelineResponseFolder]:
        
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
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterSpecificationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[outputs.PipelinePolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runDimensions")
    def run_dimensions(self) -> Optional[Mapping[str, Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Optional[Mapping[str, outputs.VariableSpecificationResponse]]:
        
        ...
    


class AwaitableGetPipelineResult(GetPipelineResult):
    def __await__(self): # -> Generator[Never, Any, GetPipelineResult]:
        ...
    


def get_pipeline(factory_name: Optional[_builtins.str] = ..., pipeline_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPipelineResult:
    
    ...

def get_pipeline_output(factory_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPipelineResult]:
    
    ...

