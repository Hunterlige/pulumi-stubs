import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCommunityTrainingResult",
    "AwaitableGetCommunityTrainingResult",
    "get_community_training",
    "get_community_training_output",
]

@pulumi.output_type
class GetCommunityTrainingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        disaster_recovery_enabled=...,
        id=...,
        identity_configuration=...,
        location=...,
        name=...,
        portal_admin_email_address=...,
        portal_name=...,
        portal_owner_email_address=...,
        portal_owner_organization_name=...,
        provisioning_state=...,
        sku=...,
        system_data=...,
        tags=...,
        type=...,
        zone_redundancy_enabled=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryEnabled")
    def disaster_recovery_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityConfiguration")
    def identity_configuration(
        self,
    ) -> outputs.IdentityConfigurationPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portalAdminEmailAddress")
    def portal_admin_email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portalName")
    def portal_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portalOwnerEmailAddress")
    def portal_owner_email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portalOwnerOrganizationName")
    def portal_owner_organization_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyEnabled")
    def zone_redundancy_enabled(self) -> _builtins.bool: ...

class AwaitableGetCommunityTrainingResult(GetCommunityTrainingResult):
    def __await__(self): ...

def get_community_training(
    community_training_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCommunityTrainingResult: ...
def get_community_training_output(
    community_training_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCommunityTrainingResult]: ...
