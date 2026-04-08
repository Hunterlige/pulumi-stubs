import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FluxConfigurationArgs", "FluxConfiguration"]

@pulumi.input_type
class FluxConfigurationArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        cluster_resource_name: pulumi.Input[_builtins.str],
        cluster_rp: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        azure_blob: Optional[pulumi.Input[AzureBlobDefinitionArgs]] = ...,
        bucket: Optional[pulumi.Input[BucketDefinitionArgs]] = ...,
        configuration_protected_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        flux_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_repository: Optional[pulumi.Input[GitRepositoryDefinitionArgs]] = ...,
        kustomizations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KustomizationDefinitionArgs]]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciliation_wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]] = ...,
        source_kind: Optional[pulumi.Input[Union[_builtins.str, SourceKindType]]] = ...,
        suspend: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceName")
    def cluster_resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_resource_name.setter
    def cluster_resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterRp")
    def cluster_rp(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_rp.setter
    def cluster_rp(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureBlob")
    def azure_blob(self) -> Optional[pulumi.Input[AzureBlobDefinitionArgs]]: ...
    @azure_blob.setter
    def azure_blob(self, value: Optional[pulumi.Input[AzureBlobDefinitionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[BucketDefinitionArgs]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[BucketDefinitionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration_protected_settings.setter
    def configuration_protected_settings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fluxConfigurationName")
    def flux_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flux_configuration_name.setter
    def flux_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitRepository")
    def git_repository(self) -> Optional[pulumi.Input[GitRepositoryDefinitionArgs]]: ...
    @git_repository.setter
    def git_repository(
        self, value: Optional[pulumi.Input[GitRepositoryDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kustomizations(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KustomizationDefinitionArgs]]]
    ]: ...
    @kustomizations.setter
    def kustomizations(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KustomizationDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reconciliationWaitDuration")
    def reconciliation_wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reconciliation_wait_duration.setter
    def reconciliation_wait_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceKind")
    def source_kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SourceKindType]]]: ...
    @source_kind.setter
    def source_kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SourceKindType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def suspend(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suspend.setter
    def suspend(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForReconciliation")
    def wait_for_reconciliation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_reconciliation.setter
    def wait_for_reconciliation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token(...)
class FluxConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        azure_blob: Optional[
            pulumi.Input[Union[AzureBlobDefinitionArgs, AzureBlobDefinitionArgsDict]]
        ] = ...,
        bucket: Optional[
            pulumi.Input[Union[BucketDefinitionArgs, BucketDefinitionArgsDict]]
        ] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_rp: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_protected_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        flux_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_repository: Optional[
            pulumi.Input[
                Union[GitRepositoryDefinitionArgs, GitRepositoryDefinitionArgsDict]
            ]
        ] = ...,
        kustomizations: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            KustomizationDefinitionArgs, KustomizationDefinitionArgsDict
                        ]
                    ],
                ]
            ]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciliation_wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]] = ...,
        source_kind: Optional[pulumi.Input[Union[_builtins.str, SourceKindType]]] = ...,
        suspend: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FluxConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FluxConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureBlob")
    def azure_blob(
        self,
    ) -> pulumi.Output[Optional[outputs.AzureBlobDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[Optional[outputs.BucketDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitRepository")
    def git_repository(
        self,
    ) -> pulumi.Output[Optional[outputs.GitRepositoryDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kustomizations(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.KustomizationDefinitionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reconciliationWaitDuration")
    def reconciliation_wait_duration(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryPublicKey")
    def repository_public_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceKind")
    def source_kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSyncedCommitId")
    def source_synced_commit_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUpdatedAt")
    def source_updated_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusUpdatedAt")
    def status_updated_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ObjectStatusDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def suspend(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="waitForReconciliation")
    def wait_for_reconciliation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
