

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyDefinitionResult', 'AwaitableGetPolicyDefinitionResult', 'get_policy_definition', 'get_policy_definition_output']
@pulumi.output_type
class GetPolicyDefinitionResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., metadata=..., mode=..., name=..., parameters=..., policy_rule=..., policy_type=..., system_data=..., type=..., version=..., versions=...) -> None:
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
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetPolicyDefinitionResult(GetPolicyDefinitionResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyDefinitionResult]:
        ...
    


def get_policy_definition(policy_definition_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyDefinitionResult:
    
    ...

def get_policy_definition_output(policy_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyDefinitionResult]:
    
    ...

