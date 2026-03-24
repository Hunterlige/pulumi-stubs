import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConsentStoreIamMemberArgs", "ConsentStoreIamMember"]

@pulumi.input_type
class ConsentStoreIamMemberArgs:
    def __init__(
        __self__,
        *,
        consent_store_id: pulumi.Input[_builtins.str],
        dataset: pulumi.Input[_builtins.str],
        member: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]] = ...,
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
    def member(self) -> pulumi.Input[_builtins.str]: ...
    @member.setter
    def member(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]]
    ): ...

@pulumi.input_type
class _ConsentStoreIamMemberState:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsentStoreIamMemberConditionArgs]]
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
    def member(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member.setter
    def member(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConsentStoreIamMember(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    ConsentStoreIamMemberConditionArgs,
                    ConsentStoreIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConsentStoreIamMemberArgs,
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
                    ConsentStoreIamMemberConditionArgs,
                    ConsentStoreIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConsentStoreIamMember: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.ConsentStoreIamMemberCondition]]: ...
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
    def member(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
