import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MembershipArgs", "Membership"]

@pulumi.input_type
class MembershipArgs:
    def __init__(
        __self__,
        *,
        collaboration_id: pulumi.Input[_builtins.str],
        query_log_status: pulumi.Input[_builtins.str],
        default_result_configuration: Optional[
            pulumi.Input[MembershipDefaultResultConfigurationArgs]
        ] = ...,
        payment_configuration: Optional[
            pulumi.Input[MembershipPaymentConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collaborationId")
    def collaboration_id(self) -> pulumi.Input[_builtins.str]: ...
    @collaboration_id.setter
    def collaboration_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Input[_builtins.str]: ...
    @query_log_status.setter
    def query_log_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResultConfiguration")
    def default_result_configuration(
        self,
    ) -> Optional[pulumi.Input[MembershipDefaultResultConfigurationArgs]]: ...
    @default_result_configuration.setter
    def default_result_configuration(
        self, value: Optional[pulumi.Input[MembershipDefaultResultConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="paymentConfiguration")
    def payment_configuration(
        self,
    ) -> Optional[pulumi.Input[MembershipPaymentConfigurationArgs]]: ...
    @payment_configuration.setter
    def payment_configuration(
        self, value: Optional[pulumi.Input[MembershipPaymentConfigurationArgs]]
    ): ...
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
class _MembershipState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_creator_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_creator_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result_configuration: Optional[
            pulumi.Input[MembershipDefaultResultConfigurationArgs]
        ] = ...,
        member_abilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        payment_configuration: Optional[
            pulumi.Input[MembershipPaymentConfigurationArgs]
        ] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collaborationArn")
    def collaboration_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_arn.setter
    def collaboration_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collaborationCreatorAccountId")
    def collaboration_creator_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_creator_account_id.setter
    def collaboration_creator_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="collaborationCreatorDisplayName")
    def collaboration_creator_display_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_creator_display_name.setter
    def collaboration_creator_display_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="collaborationId")
    def collaboration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_id.setter
    def collaboration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collaborationName")
    def collaboration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_name.setter
    def collaboration_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResultConfiguration")
    def default_result_configuration(
        self,
    ) -> Optional[pulumi.Input[MembershipDefaultResultConfigurationArgs]]: ...
    @default_result_configuration.setter
    def default_result_configuration(
        self, value: Optional[pulumi.Input[MembershipDefaultResultConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memberAbilities")
    def member_abilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @member_abilities.setter
    def member_abilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="paymentConfiguration")
    def payment_configuration(
        self,
    ) -> Optional[pulumi.Input[MembershipPaymentConfigurationArgs]]: ...
    @payment_configuration.setter
    def payment_configuration(
        self, value: Optional[pulumi.Input[MembershipPaymentConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_log_status.setter
    def query_log_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cleanrooms/membership:Membership")
class Membership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        collaboration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result_configuration: Optional[
            pulumi.Input[
                Union[
                    MembershipDefaultResultConfigurationArgs,
                    MembershipDefaultResultConfigurationArgsDict,
                ]
            ]
        ] = ...,
        payment_configuration: Optional[
            pulumi.Input[
                Union[
                    MembershipPaymentConfigurationArgs,
                    MembershipPaymentConfigurationArgsDict,
                ]
            ]
        ] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MembershipArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_creator_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_creator_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result_configuration: Optional[
            pulumi.Input[
                Union[
                    MembershipDefaultResultConfigurationArgs,
                    MembershipDefaultResultConfigurationArgsDict,
                ]
            ]
        ] = ...,
        member_abilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        payment_configuration: Optional[
            pulumi.Input[
                Union[
                    MembershipPaymentConfigurationArgs,
                    MembershipPaymentConfigurationArgsDict,
                ]
            ]
        ] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Membership: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collaborationArn")
    def collaboration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collaborationCreatorAccountId")
    def collaboration_creator_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collaborationCreatorDisplayName")
    def collaboration_creator_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collaborationId")
    def collaboration_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collaborationName")
    def collaboration_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResultConfiguration")
    def default_result_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.MembershipDefaultResultConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="memberAbilities")
    def member_abilities(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="paymentConfiguration")
    def payment_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.MembershipPaymentConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
