import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceResult",
    "AwaitableGetInstanceResult",
    "get_instance",
    "get_instance_output",
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(
        __self__,
        address=...,
        allocated_storage=...,
        auto_minor_version_upgrade=...,
        availability_zone=...,
        backup_retention_period=...,
        ca_cert_identifier=...,
        database_insights_mode=...,
        db_cluster_identifier=...,
        db_instance_arn=...,
        db_instance_class=...,
        db_instance_identifier=...,
        db_instance_port=...,
        db_name=...,
        db_parameter_groups=...,
        db_subnet_group=...,
        enabled_cloudwatch_logs_exports=...,
        endpoint=...,
        engine=...,
        engine_version=...,
        hosted_zone_id=...,
        id=...,
        iops=...,
        kms_key_id=...,
        license_model=...,
        master_user_secrets=...,
        master_username=...,
        max_allocated_storage=...,
        monitoring_interval=...,
        monitoring_role_arn=...,
        multi_az=...,
        network_type=...,
        option_group_memberships=...,
        port=...,
        preferred_backup_window=...,
        preferred_maintenance_window=...,
        publicly_accessible=...,
        region=...,
        replicate_source_db=...,
        resource_id=...,
        storage_encrypted=...,
        storage_throughput=...,
        storage_type=...,
        tags=...,
        timezone=...,
        upgrade_rollout_order=...,
        vpc_security_groups=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceArn")
    def db_instance_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceClass")
    def db_instance_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbInstancePort")
    def db_instance_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroups")
    def db_parameter_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroup")
    def db_subnet_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(
        self,
    ) -> Sequence[outputs.GetInstanceMasterUserSecretResult]: ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxAllocatedStorage")
    def max_allocated_storage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="optionGroupMemberships")
    def option_group_memberships(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicateSourceDb")
    def replicate_source_db(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="storageThroughput")
    def storage_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroups")
    def vpc_security_groups(self) -> Sequence[_builtins.str]: ...

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    db_instance_identifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    db_instance_identifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...
