import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConsentStoreIamBindingArgs", "ConsentStoreIamBinding"]

@pulumi.input_type
class ConsentStoreIamBindingArgs:
    def __init__(
        __self__,
        *,
        consent_store_id: pulumi.Input[_builtins.str],
        dataset: pulumi.Input[_builtins.str],
        members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        role: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @consent_store_id.setter
    def consent_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[_builtins.str]: ...
    @dataset.setter
    def dataset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]]
    ): ...

@pulumi.input_type
class _ConsentStoreIamBindingState:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsentStoreIamBindingConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consent_store_id.setter
    def consent_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConsentStoreIamBinding(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    ConsentStoreIamBindingConditionArgs,
                    ConsentStoreIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConsentStoreIamBindingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    ConsentStoreIamBindingConditionArgs,
                    ConsentStoreIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConsentStoreIamBinding: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.ConsentStoreIamBindingCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
