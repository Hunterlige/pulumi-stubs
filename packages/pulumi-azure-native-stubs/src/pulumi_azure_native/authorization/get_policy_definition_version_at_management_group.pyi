

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyDefinitionVersionAtManagementGroupResult', ..., 'get_policy_definition_version_at_management_group', ...]
@pulumi.output_type
class GetPolicyDefinitionVersionAtManagementGroupResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., metadata=..., mode=..., name=..., parameters=..., policy_rule=..., policy_type=..., system_data=..., type=..., version=...) -> None:
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
    


class AwaitableGetPolicyDefinitionVersionAtManagementGroupResult(GetPolicyDefinitionVersionAtManagementGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyDefinitionVersionAtManagementGroupResult]:
        ...
    


def get_policy_definition_version_at_management_group(management_group_name: Optional[_builtins.str] = ..., policy_definition_name: Optional[_builtins.str] = ..., policy_definition_version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyDefinitionVersionAtManagementGroupResult:
    
    ...

def get_policy_definition_version_at_management_group_output(management_group_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_definition_version: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyDefinitionVersionAtManagementGroupResult]:
    
    ...

