import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiFeatureStoreEntityTypeIamMemberArgs", "AiFeatureStoreEntityTypeIamMember"]

@pulumi.input_type
class AiFeatureStoreEntityTypeIamMemberArgs:
    def __init__(
        __self__,
        *,
        entitytype: pulumi.Input[_builtins.str],
        featurestore: pulumi.Input[_builtins.str],
        member: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
        condition: Optional[
            pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entitytype(self) -> pulumi.Input[_builtins.str]: ...
    @entitytype.setter
    def entitytype(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def featurestore(self) -> pulumi.Input[_builtins.str]: ...
    @featurestore.setter
    def featurestore(self, value: pulumi.Input[_builtins.str]): ...
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
    ) -> Optional[pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]],
    ): ...

@pulumi.input_type
class _AiFeatureStoreEntityTypeIamMemberState:
    def __init__(
        __self__,
        *,
        condition: Optional[
            pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]
        ] = ...,
        entitytype: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        featurestore: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[pulumi.Input[AiFeatureStoreEntityTypeIamMemberConditionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def entitytype(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entitytype.setter
    def entitytype(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def featurestore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @featurestore.setter
    def featurestore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class AiFeatureStoreEntityTypeIamMember(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    AiFeatureStoreEntityTypeIamMemberConditionArgs,
                    AiFeatureStoreEntityTypeIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        entitytype: Optional[pulumi.Input[_builtins.str]] = ...,
        featurestore: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiFeatureStoreEntityTypeIamMemberArgs,
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
                    AiFeatureStoreEntityTypeIamMemberConditionArgs,
                    AiFeatureStoreEntityTypeIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        entitytype: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        featurestore: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AiFeatureStoreEntityTypeIamMember: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiFeatureStoreEntityTypeIamMemberCondition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def entitytype(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def featurestore(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
