import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInfrastructureConfigurationResult",
    "AwaitableGetInfrastructureConfigurationResult",
    "get_infrastructure_configuration",
    "get_infrastructure_configuration_output",
]

@pulumi.output_type
class GetInfrastructureConfigurationResult:
    def __init__(
        __self__,
        arn=...,
        date_created=...,
        date_updated=...,
        description=...,
        id=...,
        instance_metadata_options=...,
        instance_profile_name=...,
        instance_types=...,
        key_pair=...,
        loggings=...,
        name=...,
        placements=...,
        region=...,
        resource_tags=...,
        security_group_ids=...,
        sns_topic_arn=...,
        subnet_id=...,
        tags=...,
        terminate_instance_on_failure=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(
        self,
    ) -> Sequence[
        outputs.GetInfrastructureConfigurationInstanceMetadataOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def loggings(
        self,
    ) -> Sequence[outputs.GetInfrastructureConfigurationLoggingResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def placements(
        self,
    ) -> Sequence[outputs.GetInfrastructureConfigurationPlacementResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> _builtins.bool: ...

class AwaitableGetInfrastructureConfigurationResult(
    GetInfrastructureConfigurationResult
):
    def __await__(self): ...

def get_infrastructure_configuration(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    resource_tags: Optional[Mapping[str, _builtins.str]] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInfrastructureConfigurationResult: ...
def get_infrastructure_configuration_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInfrastructureConfigurationResult]: ...
