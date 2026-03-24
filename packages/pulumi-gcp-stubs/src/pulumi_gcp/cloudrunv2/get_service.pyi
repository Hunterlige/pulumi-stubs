import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceResult",
    "AwaitableGetServiceResult",
    "get_service",
    "get_service_output",
]

@pulumi.output_type
class GetServiceResult:
    def __init__(
        __self__,
        annotations=...,
        binary_authorizations=...,
        build_configs=...,
        client=...,
        client_version=...,
        conditions=...,
        create_time=...,
        creator=...,
        custom_audiences=...,
        default_uri_disabled=...,
        delete_time=...,
        deletion_protection=...,
        description=...,
        effective_annotations=...,
        effective_labels=...,
        etag=...,
        expire_time=...,
        generation=...,
        iap_enabled=...,
        id=...,
        ingress=...,
        invoker_iam_disabled=...,
        labels=...,
        last_modifier=...,
        latest_created_revision=...,
        latest_ready_revision=...,
        launch_stage=...,
        location=...,
        multi_region_settings=...,
        name=...,
        observed_generation=...,
        project=...,
        pulumi_labels=...,
        reconciling=...,
        scalings=...,
        templates=...,
        terminal_conditions=...,
        traffic_statuses=...,
        traffics=...,
        uid=...,
        update_time=...,
        uri=...,
        urls=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizations")
    def binary_authorizations(
        self,
    ) -> Sequence[outputs.GetServiceBinaryAuthorizationResult]: ...
    @_builtins.property
    @pulumi.getter(name="buildConfigs")
    def build_configs(self) -> Sequence[outputs.GetServiceBuildConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetServiceConditionResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    def custom_audiences(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUriDisabled")
    def default_uri_disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iapEnabled")
    def iap_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invokerIamDisabled")
    def invoker_iam_disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionSettings")
    def multi_region_settings(
        self,
    ) -> Sequence[outputs.GetServiceMultiRegionSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def scalings(self) -> Sequence[outputs.GetServiceScalingResult]: ...
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetServiceTemplateResult]: ...
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(
        self,
    ) -> Sequence[outputs.GetServiceTerminalConditionResult]: ...
    @_builtins.property
    @pulumi.getter(name="trafficStatuses")
    def traffic_statuses(self) -> Sequence[outputs.GetServiceTrafficStatusResult]: ...
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> Sequence[outputs.GetServiceTrafficResult]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def urls(self) -> Sequence[_builtins.str]: ...

class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): ...

def get_service(
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceResult: ...
def get_service_output(
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceResult]: ...
