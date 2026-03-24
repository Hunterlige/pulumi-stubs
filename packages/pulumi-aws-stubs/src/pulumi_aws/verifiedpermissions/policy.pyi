import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyArgs", "Policy"]

@pulumi.input_type
class PolicyArgs:
    def __init__(
        __self__,
        *,
        definition: pulumi.Input[PolicyDefinitionArgs],
        policy_store_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[PolicyDefinitionArgs]: ...
    @definition.setter
    def definition(self, value: pulumi.Input[PolicyDefinitionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_store_id.setter
    def policy_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PolicyState:
    def __init__(
        __self__,
        *,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        definition: Optional[pulumi.Input[PolicyDefinitionArgs]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[PolicyDefinitionArgs]]: ...
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[PolicyDefinitionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_store_id.setter
    def policy_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:verifiedpermissions/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        definition: Optional[
            pulumi.Input[Union[PolicyDefinitionArgs, PolicyDefinitionArgsDict]]
        ] = ...,
        policy_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        definition: Optional[
            pulumi.Input[Union[PolicyDefinitionArgs, PolicyDefinitionArgsDict]]
        ] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Policy: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[outputs.PolicyDefinition]: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
