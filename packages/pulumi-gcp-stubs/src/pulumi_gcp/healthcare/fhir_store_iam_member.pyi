import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FhirStoreIamMemberArgs", "FhirStoreIamMember"]

@pulumi.input_type
class FhirStoreIamMemberArgs:
    def __init__(
        __self__,
        *,
        fhir_store_id: pulumi.Input[_builtins.str],
        member: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @fhir_store_id.setter
    def fhir_store_id(self, value: pulumi.Input[_builtins.str]): ...
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
    def condition(self) -> Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]]
    ): ...

@pulumi.input_type
class _FhirStoreIamMemberState:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        fhir_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[FhirStoreIamMemberConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fhir_store_id.setter
    def fhir_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class FhirStoreIamMember(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    FhirStoreIamMemberConditionArgs, FhirStoreIamMemberConditionArgsDict
                ]
            ]
        ] = ...,
        fhir_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FhirStoreIamMemberArgs,
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
                    FhirStoreIamMemberConditionArgs, FhirStoreIamMemberConditionArgsDict
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        fhir_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FhirStoreIamMember: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirStoreIamMemberCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
