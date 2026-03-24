import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UsageLimitArgs", "UsageLimit"]

@pulumi.input_type
class UsageLimitArgs:
    def __init__(
        __self__,
        *,
        amount: pulumi.Input[_builtins.int],
        cluster_identifier: pulumi.Input[_builtins.str],
        feature_type: pulumi.Input[_builtins.str],
        limit_type: pulumi.Input[_builtins.str],
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Input[_builtins.int]: ...
    @amount.setter
    def amount(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureType")
    def feature_type(self) -> pulumi.Input[_builtins.str]: ...
    @feature_type.setter
    def feature_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="limitType")
    def limit_type(self) -> pulumi.Input[_builtins.str]: ...
    @limit_type.setter
    def limit_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breach_action.setter
    def breach_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _UsageLimitState:
    def __init__(
        __self__,
        *,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_type: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_type: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breach_action.setter
    def breach_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featureType")
    def feature_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_type.setter
    def feature_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="limitType")
    def limit_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit_type.setter
    def limit_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:redshift/usageLimit:UsageLimit")
class UsageLimit(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_type: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_type: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UsageLimitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        amount: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        breach_action: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_type: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_type: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> UsageLimit: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="breachAction")
    def breach_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureType")
    def feature_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="limitType")
    def limit_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
