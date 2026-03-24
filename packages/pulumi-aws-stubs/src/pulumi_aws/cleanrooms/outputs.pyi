import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CollaborationDataEncryptionMetadata",
    "CollaborationMember",
    "ConfiguredTableTableReference",
    "MembershipDefaultResultConfiguration",
    ...,
    ...,
    "MembershipPaymentConfiguration",
    "MembershipPaymentConfigurationQueryCompute",
]

@pulumi.output_type
class CollaborationDataEncryptionMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_clear_text: _builtins.bool,
        allow_duplicates: _builtins.bool,
        allow_joins_on_columns_with_different_names: _builtins.bool,
        preserve_nulls: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClearText")
    def allow_clear_text(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowDuplicates")
    def allow_duplicates(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowJoinsOnColumnsWithDifferentNames")
    def allow_joins_on_columns_with_different_names(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="preserveNulls")
    def preserve_nulls(self) -> _builtins.bool: ...

@pulumi.output_type
class CollaborationMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        display_name: _builtins.str,
        member_abilities: Sequence[_builtins.str],
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memberAbilities")
    def member_abilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfiguredTableTableReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, database_name: _builtins.str, table_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...

@pulumi.output_type
class MembershipDefaultResultConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_configuration: outputs.MembershipDefaultResultConfigurationOutputConfiguration,
        role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputConfiguration")
    def output_configuration(
        self,
    ) -> outputs.MembershipDefaultResultConfigurationOutputConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipDefaultResultConfigurationOutputConfiguration(dict):
    def __init__(
        __self__,
        *,
        s3: outputs.MembershipDefaultResultConfigurationOutputConfigurationS3,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> outputs.MembershipDefaultResultConfigurationOutputConfigurationS3: ...

@pulumi.output_type
class MembershipDefaultResultConfigurationOutputConfigurationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        result_format: _builtins.str,
        key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resultFormat")
    def result_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipPaymentConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, query_compute: outputs.MembershipPaymentConfigurationQueryCompute
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryCompute")
    def query_compute(self) -> outputs.MembershipPaymentConfigurationQueryCompute: ...

@pulumi.output_type
class MembershipPaymentConfigurationQueryCompute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, is_responsible: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isResponsible")
    def is_responsible(self) -> _builtins.bool: ...
