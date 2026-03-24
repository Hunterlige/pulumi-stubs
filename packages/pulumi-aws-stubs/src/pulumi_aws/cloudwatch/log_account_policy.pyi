import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogAccountPolicyArgs", "LogAccountPolicy"]

@pulumi.input_type
class LogAccountPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_document: pulumi.Input[_builtins.str],
        policy_name: pulumi.Input[_builtins.str],
        policy_type: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        selection_criteria: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[_builtins.str]: ...
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @policy_name.setter
    def policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @policy_type.setter
    def policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selection_criteria.setter
    def selection_criteria(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogAccountPolicyState:
    def __init__(
        __self__,
        *,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        selection_criteria: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selection_criteria.setter
    def selection_criteria(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cloudwatch/logAccountPolicy:LogAccountPolicy")
class LogAccountPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        selection_criteria: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogAccountPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        selection_criteria: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LogAccountPolicy: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(self) -> pulumi.Output[Optional[_builtins.str]]: ...
