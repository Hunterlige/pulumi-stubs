import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainArgs", "Domain"]

@pulumi.input_type
class DomainArgs:
    def __init__(
        __self__,
        *,
        default_expiration_days: pulumi.Input[_builtins.int],
        domain_name: pulumi.Input[_builtins.str],
        dead_letter_queue_url: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        matching: Optional[pulumi.Input[DomainMatchingArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_based_matching: Optional[pulumi.Input[DomainRuleBasedMatchingArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultExpirationDays")
    def default_expiration_days(self) -> pulumi.Input[_builtins.int]: ...
    @default_expiration_days.setter
    def default_expiration_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionKey")
    def default_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_encryption_key.setter
    def default_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def matching(self) -> Optional[pulumi.Input[DomainMatchingArgs]]: ...
    @matching.setter
    def matching(self, value: Optional[pulumi.Input[DomainMatchingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleBasedMatching")
    def rule_based_matching(
        self,
    ) -> Optional[pulumi.Input[DomainRuleBasedMatchingArgs]]: ...
    @rule_based_matching.setter
    def rule_based_matching(
        self, value: Optional[pulumi.Input[DomainRuleBasedMatchingArgs]]
    ): ...
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
class _DomainState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dead_letter_queue_url: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_expiration_days: Optional[pulumi.Input[_builtins.int]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        matching: Optional[pulumi.Input[DomainMatchingArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_based_matching: Optional[pulumi.Input[DomainRuleBasedMatchingArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionKey")
    def default_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_encryption_key.setter
    def default_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultExpirationDays")
    def default_expiration_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_expiration_days.setter
    def default_expiration_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def matching(self) -> Optional[pulumi.Input[DomainMatchingArgs]]: ...
    @matching.setter
    def matching(self, value: Optional[pulumi.Input[DomainMatchingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleBasedMatching")
    def rule_based_matching(
        self,
    ) -> Optional[pulumi.Input[DomainRuleBasedMatchingArgs]]: ...
    @rule_based_matching.setter
    def rule_based_matching(
        self, value: Optional[pulumi.Input[DomainRuleBasedMatchingArgs]]
    ): ...
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

@pulumi.type_token("aws:customerprofiles/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dead_letter_queue_url: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_expiration_days: Optional[pulumi.Input[_builtins.int]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        matching: Optional[
            pulumi.Input[Union[DomainMatchingArgs, DomainMatchingArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_based_matching: Optional[
            pulumi.Input[
                Union[DomainRuleBasedMatchingArgs, DomainRuleBasedMatchingArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dead_letter_queue_url: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_expiration_days: Optional[pulumi.Input[_builtins.int]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        matching: Optional[
            pulumi.Input[Union[DomainMatchingArgs, DomainMatchingArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_based_matching: Optional[
            pulumi.Input[
                Union[DomainRuleBasedMatchingArgs, DomainRuleBasedMatchingArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Domain: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionKey")
    def default_encryption_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultExpirationDays")
    def default_expiration_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def matching(self) -> pulumi.Output[Optional[outputs.DomainMatching]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleBasedMatching")
    def rule_based_matching(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainRuleBasedMatching]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
