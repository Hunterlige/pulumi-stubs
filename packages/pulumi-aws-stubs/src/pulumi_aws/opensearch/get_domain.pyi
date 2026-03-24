import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDomainResult",
    "AwaitableGetDomainResult",
    "get_domain",
    "get_domain_output",
]

@pulumi.output_type
class GetDomainResult:
    def __init__(
        __self__,
        access_policies=...,
        advanced_options=...,
        advanced_security_options=...,
        arn=...,
        auto_tune_options=...,
        cluster_configs=...,
        cognito_options=...,
        created=...,
        dashboard_endpoint=...,
        dashboard_endpoint_v2=...,
        deleted=...,
        domain_endpoint_v2_hosted_zone_id=...,
        domain_id=...,
        domain_name=...,
        ebs_options=...,
        encryption_at_rests=...,
        endpoint=...,
        endpoint_v2=...,
        engine_version=...,
        id=...,
        identity_center_options=...,
        ip_address_type=...,
        log_publishing_options=...,
        node_to_node_encryptions=...,
        off_peak_window_options=...,
        processing=...,
        region=...,
        snapshot_options=...,
        software_update_options=...,
        tags=...,
        vpc_options=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> Sequence[outputs.GetDomainAdvancedSecurityOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoTuneOptions")
    def auto_tune_options(self) -> Sequence[outputs.GetDomainAutoTuneOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="clusterConfigs")
    def cluster_configs(self) -> Sequence[outputs.GetDomainClusterConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Sequence[outputs.GetDomainCognitoOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dashboardEndpoint")
    def dashboard_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dashboardEndpointV2")
    def dashboard_endpoint_v2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="domainEndpointV2HostedZoneId")
    def domain_endpoint_v2_hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Sequence[outputs.GetDomainEbsOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtRests")
    def encryption_at_rests(
        self,
    ) -> Sequence[outputs.GetDomainEncryptionAtRestResult]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointV2")
    def endpoint_v2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterOptions")
    def identity_center_options(
        self,
    ) -> Sequence[outputs.GetDomainIdentityCenterOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(
        self,
    ) -> Sequence[outputs.GetDomainLogPublishingOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeToNodeEncryptions")
    def node_to_node_encryptions(
        self,
    ) -> Sequence[outputs.GetDomainNodeToNodeEncryptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="offPeakWindowOptions")
    def off_peak_window_options(
        self,
    ) -> outputs.GetDomainOffPeakWindowOptionsResult: ...
    @_builtins.property
    @pulumi.getter
    def processing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Sequence[outputs.GetDomainSnapshotOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="softwareUpdateOptions")
    def software_update_options(
        self,
    ) -> Sequence[outputs.GetDomainSoftwareUpdateOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Sequence[outputs.GetDomainVpcOptionResult]: ...

class AwaitableGetDomainResult(GetDomainResult):
    def __await__(self): ...

def get_domain(
    domain_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDomainResult: ...
def get_domain_output(
    domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDomainResult]: ...
