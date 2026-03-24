import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DbInstanceArgs", "DbInstance"]

@pulumi.input_type
class DbInstanceArgs:
    def __init__(
        __self__,
        *,
        allocated_storage: pulumi.Input[_builtins.int],
        bucket: pulumi.Input[_builtins.str],
        db_instance_type: pulumi.Input[_builtins.str],
        organization: pulumi.Input[_builtins.str],
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        vpc_security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        db_parameter_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configuration: Optional[
            pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[DbInstanceTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Input[_builtins.int]: ...
    @allocated_storage.setter
    def allocated_storage(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceType")
    def db_instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @db_instance_type.setter
    def db_instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @vpc_subnet_ids.setter
    def vpc_subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupIdentifier")
    def db_parameter_group_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_parameter_group_identifier.setter
    def db_parameter_group_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbStorageType")
    def db_storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_storage_type.setter
    def db_storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfiguration")
    def log_delivery_configuration(
        self,
    ) -> Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]]: ...
    @log_delivery_configuration.setter
    def log_delivery_configuration(
        self, value: Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DbInstanceTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DbInstanceTimeoutsArgs]]): ...

@pulumi.input_type
class _DbInstanceState:
    def __init__(
        __self__,
        *,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        influx_auth_parameters_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configuration: Optional[
            pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[DbInstanceTimeoutsArgs]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceType")
    def db_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_type.setter
    def db_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupIdentifier")
    def db_parameter_group_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_parameter_group_identifier.setter
    def db_parameter_group_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbStorageType")
    def db_storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_storage_type.setter
    def db_storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="influxAuthParametersSecretArn")
    def influx_auth_parameters_secret_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @influx_auth_parameters_secret_arn.setter
    def influx_auth_parameters_secret_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfiguration")
    def log_delivery_configuration(
        self,
    ) -> Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]]: ...
    @log_delivery_configuration.setter
    def log_delivery_configuration(
        self, value: Optional[pulumi.Input[DbInstanceLogDeliveryConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryAvailabilityZone")
    def secondary_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_availability_zone.setter
    def secondary_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DbInstanceTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DbInstanceTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_subnet_ids.setter
    def vpc_subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:timestreaminfluxdb/dbInstance:DbInstance")
class DbInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configuration: Optional[
            pulumi.Input[
                Union[
                    DbInstanceLogDeliveryConfigurationArgs,
                    DbInstanceLogDeliveryConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[DbInstanceTimeoutsArgs, DbInstanceTimeoutsArgsDict]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DbInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        influx_auth_parameters_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configuration: Optional[
            pulumi.Input[
                Union[
                    DbInstanceLogDeliveryConfigurationArgs,
                    DbInstanceLogDeliveryConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[DbInstanceTimeoutsArgs, DbInstanceTimeoutsArgsDict]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DbInstance: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceType")
    def db_instance_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupIdentifier")
    def db_parameter_group_identifier(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbStorageType")
    def db_storage_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="influxAuthParametersSecretArn")
    def influx_auth_parameters_secret_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfiguration")
    def log_delivery_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.DbInstanceLogDeliveryConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryAvailabilityZone")
    def secondary_availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DbInstanceTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
