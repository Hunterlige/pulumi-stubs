import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalRulestackResult",
    "AwaitableGetLocalRulestackResult",
    "get_local_rulestack",
    "get_local_rulestack_output",
]

@pulumi.output_type
class GetLocalRulestackResult:
    def __init__(
        __self__,
        associated_subscriptions=...,
        azure_api_version=...,
        default_mode=...,
        description=...,
        id=...,
        identity=...,
        location=...,
        min_app_id_version=...,
        name=...,
        pan_etag=...,
        pan_location=...,
        provisioning_state=...,
        scope=...,
        security_services=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[outputs.AzureResourceManagerManagedIdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> Optional[outputs.SecurityServicesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLocalRulestackResult(GetLocalRulestackResult):
    def __await__(self): ...

def get_local_rulestack(
    local_rulestack_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalRulestackResult: ...
def get_local_rulestack_output(
    local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalRulestackResult]: ...
