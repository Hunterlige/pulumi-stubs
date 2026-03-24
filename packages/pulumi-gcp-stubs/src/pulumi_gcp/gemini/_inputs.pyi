

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CodeToolsSettingEnabledToolArgs', 'CodeToolsSettingEnabledToolArgsDict', 'CodeToolsSettingEnabledToolConfigArgs', 'CodeToolsSettingEnabledToolConfigArgsDict', 'RepositoryGroupIamBindingConditionArgs', 'RepositoryGroupIamBindingConditionArgsDict', 'RepositoryGroupIamMemberConditionArgs', 'RepositoryGroupIamMemberConditionArgsDict', 'RepositoryGroupRepositoryArgs', 'RepositoryGroupRepositoryArgsDict']
class CodeToolsSettingEnabledToolArgsDict(TypedDict):
    handle: pulumi.Input[_builtins.str]
    tool: pulumi.Input[_builtins.str]
    account_connector: NotRequired[pulumi.Input[_builtins.str]]
    configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[CodeToolsSettingEnabledToolConfigArgsDict]]]]
    uri_override: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CodeToolsSettingEnabledToolArgs:
    def __init__(__self__, *, handle: pulumi.Input[_builtins.str], tool: pulumi.Input[_builtins.str], account_connector: Optional[pulumi.Input[_builtins.str]] = ..., configs: Optional[pulumi.Input[Sequence[pulumi.Input[CodeToolsSettingEnabledToolConfigArgs]]]] = ..., uri_override: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def handle(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @handle.setter
    def handle(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tool.setter
    def tool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountConnector")
    def account_connector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_connector.setter
    def account_connector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CodeToolsSettingEnabledToolConfigArgs]]]]:
        
        ...
    
    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CodeToolsSettingEnabledToolConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriOverride")
    def uri_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri_override.setter
    def uri_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CodeToolsSettingEnabledToolConfigArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class CodeToolsSettingEnabledToolConfigArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RepositoryGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RepositoryGroupIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RepositoryGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RepositoryGroupIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RepositoryGroupRepositoryArgsDict(TypedDict):
    branch_pattern: pulumi.Input[_builtins.str]
    resource: pulumi.Input[_builtins.str]


@pulumi.input_type
class RepositoryGroupRepositoryArgs:
    def __init__(__self__, *, branch_pattern: pulumi.Input[_builtins.str], resource: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchPattern")
    def branch_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @branch_pattern.setter
    def branch_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


