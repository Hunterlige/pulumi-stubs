import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppProfileArgs", "AppProfile"]

@pulumi.input_type
class AppProfileArgs:
    def __init__(
        __self__,
        *,
        app_profile_id: pulumi.Input[_builtins.str],
        data_boost_isolation_read_only: Optional[
            pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_cluster_routing_cluster_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_cluster_routing_use_any: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        single_cluster_routing: Optional[
            pulumi.Input[AppProfileSingleClusterRoutingArgs]
        ] = ...,
        standard_isolation: Optional[
            pulumi.Input[AppProfileStandardIsolationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_profile_id.setter
    def app_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataBoostIsolationReadOnly")
    def data_boost_isolation_read_only(
        self,
    ) -> Optional[pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]]: ...
    @data_boost_isolation_read_only.setter
    def data_boost_isolation_read_only(
        self, value: Optional[pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingClusterIds")
    def multi_cluster_routing_cluster_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @multi_cluster_routing_cluster_ids.setter
    def multi_cluster_routing_cluster_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingUseAny")
    def multi_cluster_routing_use_any(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_cluster_routing_use_any.setter
    def multi_cluster_routing_use_any(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowAffinity")
    def row_affinity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @row_affinity.setter
    def row_affinity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="singleClusterRouting")
    def single_cluster_routing(
        self,
    ) -> Optional[pulumi.Input[AppProfileSingleClusterRoutingArgs]]: ...
    @single_cluster_routing.setter
    def single_cluster_routing(
        self, value: Optional[pulumi.Input[AppProfileSingleClusterRoutingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standardIsolation")
    def standard_isolation(
        self,
    ) -> Optional[pulumi.Input[AppProfileStandardIsolationArgs]]: ...
    @standard_isolation.setter
    def standard_isolation(
        self, value: Optional[pulumi.Input[AppProfileStandardIsolationArgs]]
    ): ...

@pulumi.input_type
class _AppProfileState:
    def __init__(
        __self__,
        *,
        app_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_boost_isolation_read_only: Optional[
            pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_cluster_routing_cluster_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_cluster_routing_use_any: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        single_cluster_routing: Optional[
            pulumi.Input[AppProfileSingleClusterRoutingArgs]
        ] = ...,
        standard_isolation: Optional[
            pulumi.Input[AppProfileStandardIsolationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_profile_id.setter
    def app_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataBoostIsolationReadOnly")
    def data_boost_isolation_read_only(
        self,
    ) -> Optional[pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]]: ...
    @data_boost_isolation_read_only.setter
    def data_boost_isolation_read_only(
        self, value: Optional[pulumi.Input[AppProfileDataBoostIsolationReadOnlyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_warnings.setter
    def ignore_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingClusterIds")
    def multi_cluster_routing_cluster_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @multi_cluster_routing_cluster_ids.setter
    def multi_cluster_routing_cluster_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingUseAny")
    def multi_cluster_routing_use_any(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_cluster_routing_use_any.setter
    def multi_cluster_routing_use_any(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowAffinity")
    def row_affinity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @row_affinity.setter
    def row_affinity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="singleClusterRouting")
    def single_cluster_routing(
        self,
    ) -> Optional[pulumi.Input[AppProfileSingleClusterRoutingArgs]]: ...
    @single_cluster_routing.setter
    def single_cluster_routing(
        self, value: Optional[pulumi.Input[AppProfileSingleClusterRoutingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standardIsolation")
    def standard_isolation(
        self,
    ) -> Optional[pulumi.Input[AppProfileStandardIsolationArgs]]: ...
    @standard_isolation.setter
    def standard_isolation(
        self, value: Optional[pulumi.Input[AppProfileStandardIsolationArgs]]
    ): ...

@pulumi.type_token("gcp:bigtable/appProfile:AppProfile")
class AppProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_boost_isolation_read_only: Optional[
            pulumi.Input[
                Union[
                    AppProfileDataBoostIsolationReadOnlyArgs,
                    AppProfileDataBoostIsolationReadOnlyArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_cluster_routing_cluster_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_cluster_routing_use_any: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        single_cluster_routing: Optional[
            pulumi.Input[
                Union[
                    AppProfileSingleClusterRoutingArgs,
                    AppProfileSingleClusterRoutingArgsDict,
                ]
            ]
        ] = ...,
        standard_isolation: Optional[
            pulumi.Input[
                Union[
                    AppProfileStandardIsolationArgs, AppProfileStandardIsolationArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_boost_isolation_read_only: Optional[
            pulumi.Input[
                Union[
                    AppProfileDataBoostIsolationReadOnlyArgs,
                    AppProfileDataBoostIsolationReadOnlyArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_cluster_routing_cluster_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_cluster_routing_use_any: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        single_cluster_routing: Optional[
            pulumi.Input[
                Union[
                    AppProfileSingleClusterRoutingArgs,
                    AppProfileSingleClusterRoutingArgsDict,
                ]
            ]
        ] = ...,
        standard_isolation: Optional[
            pulumi.Input[
                Union[
                    AppProfileStandardIsolationArgs, AppProfileStandardIsolationArgsDict
                ]
            ]
        ] = ...,
    ) -> AppProfile: ...
    @_builtins.property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataBoostIsolationReadOnly")
    def data_boost_isolation_read_only(
        self,
    ) -> pulumi.Output[Optional[outputs.AppProfileDataBoostIsolationReadOnly]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreWarnings")
    def ignore_warnings(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingClusterIds")
    def multi_cluster_routing_cluster_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="multiClusterRoutingUseAny")
    def multi_cluster_routing_use_any(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rowAffinity")
    def row_affinity(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="singleClusterRouting")
    def single_cluster_routing(
        self,
    ) -> pulumi.Output[Optional[outputs.AppProfileSingleClusterRouting]]: ...
    @_builtins.property
    @pulumi.getter(name="standardIsolation")
    def standard_isolation(
        self,
    ) -> pulumi.Output[outputs.AppProfileStandardIsolation]: ...
