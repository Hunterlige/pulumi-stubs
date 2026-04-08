import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectorDryrunArgs", "ConnectorDryrun"]

@pulumi.input_type
class ConnectorDryrunArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        dryrun_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dryrunName")
    def dryrun_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dryrun_name.setter
    def dryrun_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[CreateOrUpdateDryrunParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:servicelinker:ConnectorDryrun")
class ConnectorDryrun(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dryrun_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Union[
                    CreateOrUpdateDryrunParametersArgs,
                    CreateOrUpdateDryrunParametersArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectorDryrunArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConnectorDryrun: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationPreviews")
    def operation_previews(
        self,
    ) -> pulumi.Output[Sequence[outputs.DryrunOperationPreviewResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[outputs.CreateOrUpdateDryrunParametersResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="prerequisiteResults")
    def prerequisite_results(self) -> pulumi.Output[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
