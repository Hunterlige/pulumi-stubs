import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RowAccessPolicyArgs", "RowAccessPolicy"]

@pulumi.input_type
class RowAccessPolicyArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        filter_predicate: pulumi.Input[_builtins.str],
        policy_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterPredicate")
    def filter_predicate(self) -> pulumi.Input[_builtins.str]: ...
    @filter_predicate.setter
    def filter_predicate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def grantees(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grantees.setter
    def grantees(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RowAccessPolicyState:
    def __init__(
        __self__,
        *,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_predicate: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterPredicate")
    def filter_predicate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter_predicate.setter
    def filter_predicate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def grantees(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grantees.setter
    def grantees(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigquery/rowAccessPolicy:RowAccessPolicy")
class RowAccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_predicate: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RowAccessPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_predicate: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RowAccessPolicy: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterPredicate")
    def filter_predicate(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grantees(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Output[_builtins.str]: ...
