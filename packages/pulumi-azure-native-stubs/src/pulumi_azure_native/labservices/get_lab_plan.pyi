import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLabPlanResult",
    "AwaitableGetLabPlanResult",
    "get_lab_plan",
    "get_lab_plan_output",
]

@pulumi.output_type
class GetLabPlanResult:
    def __init__(
        __self__,
        allowed_regions=...,
        azure_api_version=...,
        default_auto_shutdown_profile=...,
        default_connection_profile=...,
        default_network_profile=...,
        id=...,
        identity=...,
        linked_lms_instance=...,
        location=...,
        name=...,
        provisioning_state=...,
        resource_operation_error=...,
        shared_gallery_id=...,
        support_info=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(
        self,
    ) -> Optional[outputs.AutoShutdownProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(
        self,
    ) -> Optional[outputs.ConnectionProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(
        self,
    ) -> Optional[outputs.LabPlanNetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> outputs.ResourceOperationErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> Optional[outputs.SupportInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLabPlanResult(GetLabPlanResult):
    def __await__(self): ...

def get_lab_plan(
    lab_plan_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLabPlanResult: ...
def get_lab_plan_output(
    lab_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLabPlanResult]: ...
