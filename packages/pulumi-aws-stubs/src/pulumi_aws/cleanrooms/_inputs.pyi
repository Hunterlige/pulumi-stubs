import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CollaborationDataEncryptionMetadataArgs",
    "CollaborationDataEncryptionMetadataArgsDict",
    "CollaborationMemberArgs",
    "CollaborationMemberArgsDict",
    "ConfiguredTableTableReferenceArgs",
    "ConfiguredTableTableReferenceArgsDict",
    "MembershipDefaultResultConfigurationArgs",
    "MembershipDefaultResultConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "MembershipPaymentConfigurationArgs",
    "MembershipPaymentConfigurationArgsDict",
    "MembershipPaymentConfigurationQueryComputeArgs",
    "MembershipPaymentConfigurationQueryComputeArgsDict",
]

class CollaborationDataEncryptionMetadataArgsDict(TypedDict):
    allow_clear_text: pulumi.Input[_builtins.bool]
    allow_duplicates: pulumi.Input[_builtins.bool]
    allow_joins_on_columns_with_different_names: pulumi.Input[_builtins.bool]
    preserve_nulls: pulumi.Input[_builtins.bool]

@pulumi.input_type
class CollaborationDataEncryptionMetadataArgs:
    def __init__(
        __self__,
        *,
        allow_clear_text: pulumi.Input[_builtins.bool],
        allow_duplicates: pulumi.Input[_builtins.bool],
        allow_joins_on_columns_with_different_names: pulumi.Input[_builtins.bool],
        preserve_nulls: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClearText")
    def allow_clear_text(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_clear_text.setter
    def allow_clear_text(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="allowDuplicates")
    def allow_duplicates(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_duplicates.setter
    def allow_duplicates(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="allowJoinsOnColumnsWithDifferentNames")
    def allow_joins_on_columns_with_different_names(
        self,
    ) -> pulumi.Input[_builtins.bool]: ...
    @allow_joins_on_columns_with_different_names.setter
    def allow_joins_on_columns_with_different_names(
        self, value: pulumi.Input[_builtins.bool]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preserveNulls")
    def preserve_nulls(self) -> pulumi.Input[_builtins.bool]: ...
    @preserve_nulls.setter
    def preserve_nulls(self, value: pulumi.Input[_builtins.bool]): ...

class CollaborationMemberArgsDict(TypedDict):
    account_id: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    member_abilities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CollaborationMemberArgs:
    def __init__(
        __self__,
        *,
        account_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        member_abilities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="memberAbilities")
    def member_abilities(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @member_abilities.setter
    def member_abilities(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfiguredTableTableReferenceArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConfiguredTableTableReferenceArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...

class MembershipDefaultResultConfigurationArgsDict(TypedDict):
    output_configuration: pulumi.Input[
        MembershipDefaultResultConfigurationOutputConfigurationArgsDict
    ]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MembershipDefaultResultConfigurationArgs:
    def __init__(
        __self__,
        *,
        output_configuration: pulumi.Input[
            MembershipDefaultResultConfigurationOutputConfigurationArgs
        ],
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputConfiguration")
    def output_configuration(
        self,
    ) -> pulumi.Input[MembershipDefaultResultConfigurationOutputConfigurationArgs]: ...
    @output_configuration.setter
    def output_configuration(
        self,
        value: pulumi.Input[
            MembershipDefaultResultConfigurationOutputConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MembershipDefaultResultConfigurationOutputConfigurationArgsDict(TypedDict):
    s3: pulumi.Input[MembershipDefaultResultConfigurationOutputConfigurationS3ArgsDict]

@pulumi.input_type
class MembershipDefaultResultConfigurationOutputConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3: pulumi.Input[MembershipDefaultResultConfigurationOutputConfigurationS3Args],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> pulumi.Input[
        MembershipDefaultResultConfigurationOutputConfigurationS3Args
    ]: ...
    @s3.setter
    def s3(
        self,
        value: pulumi.Input[
            MembershipDefaultResultConfigurationOutputConfigurationS3Args
        ],
    ): ...

class MembershipDefaultResultConfigurationOutputConfigurationS3ArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    result_format: pulumi.Input[_builtins.str]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MembershipDefaultResultConfigurationOutputConfigurationS3Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        result_format: pulumi.Input[_builtins.str],
        key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resultFormat")
    def result_format(self) -> pulumi.Input[_builtins.str]: ...
    @result_format.setter
    def result_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MembershipPaymentConfigurationArgsDict(TypedDict):
    query_compute: pulumi.Input[MembershipPaymentConfigurationQueryComputeArgsDict]

@pulumi.input_type
class MembershipPaymentConfigurationArgs:
    def __init__(
        __self__,
        *,
        query_compute: pulumi.Input[MembershipPaymentConfigurationQueryComputeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryCompute")
    def query_compute(
        self,
    ) -> pulumi.Input[MembershipPaymentConfigurationQueryComputeArgs]: ...
    @query_compute.setter
    def query_compute(
        self, value: pulumi.Input[MembershipPaymentConfigurationQueryComputeArgs]
    ): ...

class MembershipPaymentConfigurationQueryComputeArgsDict(TypedDict):
    is_responsible: pulumi.Input[_builtins.bool]

@pulumi.input_type
class MembershipPaymentConfigurationQueryComputeArgs:
    def __init__(__self__, *, is_responsible: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isResponsible")
    def is_responsible(self) -> pulumi.Input[_builtins.bool]: ...
    @is_responsible.setter
    def is_responsible(self, value: pulumi.Input[_builtins.bool]): ...
