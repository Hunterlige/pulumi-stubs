import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AiFeatureOnlineStoreFeatureviewIamBindingArgs",
    "AiFeatureOnlineStoreFeatureviewIamBinding",
]

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewIamBindingArgs:
    def __init__(
        __self__,
        *,
        feature_online_store: pulumi.Input[_builtins.str],
        feature_view: pulumi.Input[_builtins.str],
        members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        role: pulumi.Input[_builtins.str],
        condition: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> pulumi.Input[_builtins.str]: ...
    @feature_online_store.setter
    def feature_online_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureView")
    def feature_view(self) -> pulumi.Input[_builtins.str]: ...
    @feature_view.setter
    def feature_view(self, value: pulumi.Input[_builtins.str]): ...
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
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AiFeatureOnlineStoreFeatureviewIamBindingState:
    def __init__(
        __self__,
        *,
        condition: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_view: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_online_store.setter
    def feature_online_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featureView")
    def feature_view(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_view.setter
    def feature_view(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AiFeatureOnlineStoreFeatureviewIamBinding(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs,
                    AiFeatureOnlineStoreFeatureviewIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_view: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiFeatureOnlineStoreFeatureviewIamBindingArgs,
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
                    AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs,
                    AiFeatureOnlineStoreFeatureviewIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_view: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AiFeatureOnlineStoreFeatureviewIamBinding: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiFeatureOnlineStoreFeatureviewIamBindingCondition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureView")
    def feature_view(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
