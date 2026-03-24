import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterClusterNode",
    "EndpointAccessVpcEndpoint",
    "EndpointAccessVpcEndpointNetworkInterface",
    "IdcApplicationAuthorizedTokenIssuer",
    "IdcApplicationServiceIntegration",
    "IdcApplicationServiceIntegrationLakeFormation",
    ...,
    "IdcApplicationServiceIntegrationRedshift",
    "IdcApplicationServiceIntegrationRedshiftConnect",
    "IdcApplicationServiceIntegrationS3AccessGrants",
    ...,
    "IntegrationTimeouts",
    "ParameterGroupParameter",
    "ScheduledActionTargetAction",
    "ScheduledActionTargetActionPauseCluster",
    "ScheduledActionTargetActionResizeCluster",
    "ScheduledActionTargetActionResumeCluster",
    "GetClusterClusterNodeResult",
    "GetDataSharesDataShareResult",
    "GetProducerDataSharesDataShareResult",
]

@pulumi.output_type
class ClusterClusterNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_role: Optional[_builtins.str] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        public_ip_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointAccessVpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_interfaces: Optional[
            Sequence[outputs.EndpointAccessVpcEndpointNetworkInterface]
        ] = ...,
        vpc_endpoint_id: Optional[_builtins.str] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[Sequence[outputs.EndpointAccessVpcEndpointNetworkInterface]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointAccessVpcEndpointNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone: Optional[_builtins.str] = ...,
        network_interface_id: Optional[_builtins.str] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        subnet_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdcApplicationAuthorizedTokenIssuer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorized_audiences_lists: Optional[Sequence[_builtins.str]] = ...,
        trusted_token_issuer_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedAudiencesLists")
    def authorized_audiences_lists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerArn")
    def trusted_token_issuer_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdcApplicationServiceIntegration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lake_formation: Optional[
            outputs.IdcApplicationServiceIntegrationLakeFormation
        ] = ...,
        redshift: Optional[outputs.IdcApplicationServiceIntegrationRedshift] = ...,
        s3_access_grants: Optional[
            outputs.IdcApplicationServiceIntegrationS3AccessGrants
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lakeFormation")
    def lake_formation(
        self,
    ) -> Optional[outputs.IdcApplicationServiceIntegrationLakeFormation]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(
        self,
    ) -> Optional[outputs.IdcApplicationServiceIntegrationRedshift]: ...
    @_builtins.property
    @pulumi.getter(name="s3AccessGrants")
    def s3_access_grants(
        self,
    ) -> Optional[outputs.IdcApplicationServiceIntegrationS3AccessGrants]: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationLakeFormation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lake_formation_query: Optional[
            outputs.IdcApplicationServiceIntegrationLakeFormationLakeFormationQuery
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lakeFormationQuery")
    def lake_formation_query(
        self,
    ) -> Optional[
        outputs.IdcApplicationServiceIntegrationLakeFormationLakeFormationQuery
    ]: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationLakeFormationLakeFormationQuery(dict):
    def __init__(__self__, *, authorization: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> _builtins.str: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationRedshift(dict):
    def __init__(
        __self__,
        *,
        connect: Optional[
            outputs.IdcApplicationServiceIntegrationRedshiftConnect
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connect(
        self,
    ) -> Optional[outputs.IdcApplicationServiceIntegrationRedshiftConnect]: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationRedshiftConnect(dict):
    def __init__(__self__, *, authorization: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> _builtins.str: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationS3AccessGrants(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        read_write_access: Optional[
            outputs.IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccess
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readWriteAccess")
    def read_write_access(
        self,
    ) -> Optional[
        outputs.IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccess
    ]: ...

@pulumi.output_type
class IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccess(dict):
    def __init__(__self__, *, authorization: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> _builtins.str: ...

@pulumi.output_type
class IntegrationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ParameterGroupParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduledActionTargetAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pause_cluster: Optional[outputs.ScheduledActionTargetActionPauseCluster] = ...,
        resize_cluster: Optional[
            outputs.ScheduledActionTargetActionResizeCluster
        ] = ...,
        resume_cluster: Optional[
            outputs.ScheduledActionTargetActionResumeCluster
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pauseCluster")
    def pause_cluster(
        self,
    ) -> Optional[outputs.ScheduledActionTargetActionPauseCluster]: ...
    @_builtins.property
    @pulumi.getter(name="resizeCluster")
    def resize_cluster(
        self,
    ) -> Optional[outputs.ScheduledActionTargetActionResizeCluster]: ...
    @_builtins.property
    @pulumi.getter(name="resumeCluster")
    def resume_cluster(
        self,
    ) -> Optional[outputs.ScheduledActionTargetActionResumeCluster]: ...

@pulumi.output_type
class ScheduledActionTargetActionPauseCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cluster_identifier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduledActionTargetActionResizeCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_identifier: _builtins.str,
        classic: Optional[_builtins.bool] = ...,
        cluster_type: Optional[_builtins.str] = ...,
        node_type: Optional[_builtins.str] = ...,
        number_of_nodes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def classic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledActionTargetActionResumeCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cluster_identifier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterNodeResult(dict):
    def __init__(
        __self__,
        *,
        node_role: _builtins.str,
        private_ip_address: _builtins.str,
        public_ip_address: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSharesDataShareResult(dict):
    def __init__(
        __self__,
        *,
        data_share_arn: _builtins.str,
        managed_by: _builtins.str,
        producer_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetProducerDataSharesDataShareResult(dict):
    def __init__(
        __self__,
        *,
        data_share_arn: _builtins.str,
        managed_by: _builtins.str,
        producer_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> _builtins.str: ...
