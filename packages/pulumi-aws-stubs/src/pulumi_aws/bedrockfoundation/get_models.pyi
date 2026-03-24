

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetModelsResult', 'AwaitableGetModelsResult', 'get_models', 'get_models_output']
@pulumi.output_type
class GetModelsResult:
    
    def __init__(__self__, by_customization_type=..., by_inference_type=..., by_output_modality=..., by_provider=..., id=..., model_summaries=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="byCustomizationType")
    def by_customization_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="byInferenceType")
    def by_inference_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="byOutputModality")
    def by_output_modality(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="byProvider")
    def by_provider(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSummaries")
    def model_summaries(self) -> Sequence[outputs.GetModelsModelSummaryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetModelsResult(GetModelsResult):
    def __await__(self): # -> Generator[Never, Any, GetModelsResult]:
        ...
    


def get_models(by_customization_type: Optional[_builtins.str] = ..., by_inference_type: Optional[_builtins.str] = ..., by_output_modality: Optional[_builtins.str] = ..., by_provider: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetModelsResult:
    
    ...

def get_models_output(by_customization_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., by_inference_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., by_output_modality: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., by_provider: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetModelsResult]:
    
    ...

