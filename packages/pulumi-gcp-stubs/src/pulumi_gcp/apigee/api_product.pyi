import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiProductArgs", "ApiProduct"]

@pulumi.input_type
class ApiProductArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        api_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approval_type: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        graphql_operation_group: Optional[
            pulumi.Input[ApiProductGraphqlOperationGroupArgs]
        ] = ...,
        grpc_operation_group: Optional[
            pulumi.Input[ApiProductGrpcOperationGroupArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_group: Optional[pulumi.Input[ApiProductOperationGroupArgs]] = ...,
        proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        quota: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_counter_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        space: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiResources")
    def api_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @api_resources.setter
    def api_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalType")
    def approval_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approval_type.setter
    def approval_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]]: ...
    @attributes.setter
    def attributes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @environments.setter
    def environments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="graphqlOperationGroup")
    def graphql_operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductGraphqlOperationGroupArgs]]: ...
    @graphql_operation_group.setter
    def graphql_operation_group(
        self, value: Optional[pulumi.Input[ApiProductGraphqlOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcOperationGroup")
    def grpc_operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductGrpcOperationGroupArgs]]: ...
    @grpc_operation_group.setter
    def grpc_operation_group(
        self, value: Optional[pulumi.Input[ApiProductGrpcOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationGroup")
    def operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductOperationGroupArgs]]: ...
    @operation_group.setter
    def operation_group(
        self, value: Optional[pulumi.Input[ApiProductOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def proxies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @proxies.setter
    def proxies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaCounterScope")
    def quota_counter_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_counter_scope.setter
    def quota_counter_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaInterval")
    def quota_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_interval.setter
    def quota_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaTimeUnit")
    def quota_time_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_time_unit.setter
    def quota_time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space.setter
    def space(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ApiProductState:
    def __init__(
        __self__,
        *,
        api_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approval_type: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]
        ] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        graphql_operation_group: Optional[
            pulumi.Input[ApiProductGraphqlOperationGroupArgs]
        ] = ...,
        grpc_operation_group: Optional[
            pulumi.Input[ApiProductGrpcOperationGroupArgs]
        ] = ...,
        last_modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_group: Optional[pulumi.Input[ApiProductOperationGroupArgs]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        quota: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_counter_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        space: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiResources")
    def api_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @api_resources.setter
    def api_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalType")
    def approval_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approval_type.setter
    def approval_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]]: ...
    @attributes.setter
    def attributes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductAttributeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @environments.setter
    def environments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="graphqlOperationGroup")
    def graphql_operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductGraphqlOperationGroupArgs]]: ...
    @graphql_operation_group.setter
    def graphql_operation_group(
        self, value: Optional[pulumi.Input[ApiProductGraphqlOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcOperationGroup")
    def grpc_operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductGrpcOperationGroupArgs]]: ...
    @grpc_operation_group.setter
    def grpc_operation_group(
        self, value: Optional[pulumi.Input[ApiProductGrpcOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationGroup")
    def operation_group(
        self,
    ) -> Optional[pulumi.Input[ApiProductOperationGroupArgs]]: ...
    @operation_group.setter
    def operation_group(
        self, value: Optional[pulumi.Input[ApiProductOperationGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def proxies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @proxies.setter
    def proxies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaCounterScope")
    def quota_counter_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_counter_scope.setter
    def quota_counter_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaInterval")
    def quota_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_interval.setter
    def quota_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaTimeUnit")
    def quota_time_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_time_unit.setter
    def quota_time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space.setter
    def space(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:apigee/apiProduct:ApiProduct")
class ApiProduct(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approval_type: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApiProductAttributeArgs, ApiProductAttributeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        graphql_operation_group: Optional[
            pulumi.Input[
                Union[
                    ApiProductGraphqlOperationGroupArgs,
                    ApiProductGraphqlOperationGroupArgsDict,
                ]
            ]
        ] = ...,
        grpc_operation_group: Optional[
            pulumi.Input[
                Union[
                    ApiProductGrpcOperationGroupArgs,
                    ApiProductGrpcOperationGroupArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_group: Optional[
            pulumi.Input[
                Union[ApiProductOperationGroupArgs, ApiProductOperationGroupArgsDict]
            ]
        ] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        quota: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_counter_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        space: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiProductArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approval_type: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApiProductAttributeArgs, ApiProductAttributeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        graphql_operation_group: Optional[
            pulumi.Input[
                Union[
                    ApiProductGraphqlOperationGroupArgs,
                    ApiProductGraphqlOperationGroupArgsDict,
                ]
            ]
        ] = ...,
        grpc_operation_group: Optional[
            pulumi.Input[
                Union[
                    ApiProductGrpcOperationGroupArgs,
                    ApiProductGrpcOperationGroupArgsDict,
                ]
            ]
        ] = ...,
        last_modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_group: Optional[
            pulumi.Input[
                Union[ApiProductOperationGroupArgs, ApiProductOperationGroupArgsDict]
            ]
        ] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        quota: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_counter_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        quota_time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        space: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ApiProduct: ...
    @_builtins.property
    @pulumi.getter(name="apiResources")
    def api_resources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="approvalType")
    def approval_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApiProductAttribute]]]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environments(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="graphqlOperationGroup")
    def graphql_operation_group(
        self,
    ) -> pulumi.Output[Optional[outputs.ApiProductGraphqlOperationGroup]]: ...
    @_builtins.property
    @pulumi.getter(name="grpcOperationGroup")
    def grpc_operation_group(
        self,
    ) -> pulumi.Output[Optional[outputs.ApiProductGrpcOperationGroup]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationGroup")
    def operation_group(
        self,
    ) -> pulumi.Output[Optional[outputs.ApiProductOperationGroup]]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def proxies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def quota(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="quotaCounterScope")
    def quota_counter_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="quotaInterval")
    def quota_interval(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="quotaTimeUnit")
    def quota_time_unit(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def space(self) -> pulumi.Output[Optional[_builtins.str]]: ...
