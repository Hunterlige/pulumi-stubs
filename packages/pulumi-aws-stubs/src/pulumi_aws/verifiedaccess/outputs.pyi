import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EndpointCidrOptions",
    "EndpointCidrOptionsPortRange",
    "EndpointLoadBalancerOptions",
    "EndpointLoadBalancerOptionsPortRange",
    "EndpointNetworkInterfaceOptions",
    "EndpointNetworkInterfaceOptionsPortRange",
    "EndpointRdsOptions",
    "EndpointSseSpecification",
    "GroupSseConfiguration",
    "InstanceLoggingConfigurationAccessLogs",
    ...,
    ...,
    "InstanceLoggingConfigurationAccessLogsS3",
    "InstanceVerifiedAccessTrustProvider",
    "TrustProviderDeviceOptions",
    "TrustProviderNativeApplicationOidcOptions",
    "TrustProviderOidcOptions",
    "TrustProviderSseSpecification",
]

@pulumi.output_type
class EndpointCidrOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cidr: _builtins.str,
        port_ranges: Sequence[outputs.EndpointCidrOptionsPortRange],
        protocol: Optional[_builtins.str] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.EndpointCidrOptionsPortRange]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointCidrOptionsPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_port: _builtins.int, to_port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointLoadBalancerOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        load_balancer_arn: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        port_ranges: Optional[
            Sequence[outputs.EndpointLoadBalancerOptionsPortRange]
        ] = ...,
        protocol: Optional[_builtins.str] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[Sequence[outputs.EndpointLoadBalancerOptionsPortRange]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointLoadBalancerOptionsPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_port: _builtins.int, to_port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointNetworkInterfaceOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_interface_id: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        port_ranges: Optional[
            Sequence[outputs.EndpointNetworkInterfaceOptionsPortRange]
        ] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[Sequence[outputs.EndpointNetworkInterfaceOptionsPortRange]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointNetworkInterfaceOptionsPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_port: _builtins.int, to_port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointRdsOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        protocol: Optional[_builtins.str] = ...,
        rds_db_cluster_arn: Optional[_builtins.str] = ...,
        rds_db_instance_arn: Optional[_builtins.str] = ...,
        rds_db_proxy_arn: Optional[_builtins.str] = ...,
        rds_endpoint: Optional[_builtins.str] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdsDbClusterArn")
    def rds_db_cluster_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdsDbInstanceArn")
    def rds_db_instance_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdsDbProxyArn")
    def rds_db_proxy_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdsEndpoint")
    def rds_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointSseSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_managed_key_enabled: Optional[_builtins.bool] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GroupSseConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_managed_key_enabled: Optional[_builtins.bool] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceLoggingConfigurationAccessLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            outputs.InstanceLoggingConfigurationAccessLogsCloudwatchLogs
        ] = ...,
        include_trust_context: Optional[_builtins.bool] = ...,
        kinesis_data_firehose: Optional[
            outputs.InstanceLoggingConfigurationAccessLogsKinesisDataFirehose
        ] = ...,
        log_version: Optional[_builtins.str] = ...,
        s3: Optional[outputs.InstanceLoggingConfigurationAccessLogsS3] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[outputs.InstanceLoggingConfigurationAccessLogsCloudwatchLogs]: ...
    @_builtins.property
    @pulumi.getter(name="includeTrustContext")
    def include_trust_context(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisDataFirehose")
    def kinesis_data_firehose(
        self,
    ) -> Optional[
        outputs.InstanceLoggingConfigurationAccessLogsKinesisDataFirehose
    ]: ...
    @_builtins.property
    @pulumi.getter(name="logVersion")
    def log_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.InstanceLoggingConfigurationAccessLogsS3]: ...

@pulumi.output_type
class InstanceLoggingConfigurationAccessLogsCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, log_group: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceLoggingConfigurationAccessLogsKinesisDataFirehose(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        delivery_stream: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceLoggingConfigurationAccessLogsS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_owner: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceVerifiedAccessTrustProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        device_trust_provider_type: Optional[_builtins.str] = ...,
        trust_provider_type: Optional[_builtins.str] = ...,
        user_trust_provider_type: Optional[_builtins.str] = ...,
        verified_access_trust_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifiedAccessTrustProviderId")
    def verified_access_trust_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustProviderDeviceOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, tenant_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustProviderNativeApplicationOidcOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_secret: _builtins.str,
        authorization_endpoint: Optional[_builtins.str] = ...,
        client_id: Optional[_builtins.str] = ...,
        issuer: Optional[_builtins.str] = ...,
        public_signing_key_endpoint: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        token_endpoint: Optional[_builtins.str] = ...,
        user_info_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicSigningKeyEndpoint")
    def public_signing_key_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustProviderOidcOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_secret: _builtins.str,
        authorization_endpoint: Optional[_builtins.str] = ...,
        client_id: Optional[_builtins.str] = ...,
        issuer: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        token_endpoint: Optional[_builtins.str] = ...,
        user_info_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustProviderSseSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_managed_key_enabled: Optional[_builtins.bool] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
