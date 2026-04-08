import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ActionRequestArgs", "ActionRequest"]

@pulumi.input_type
class ActionRequestArgs:
    def __init__(
        __self__,
        *,
        request_type: pulumi.Input[Union[_builtins.str, RequestTypes]],
        resource_group_name: pulumi.Input[_builtins.str],
        test_base_account_name: pulumi.Input[_builtins.str],
        action_request_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_release_access_request_spec: Optional[
            pulumi.Input[PreReleaseAccessRequestSpecArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestType")
    def request_type(self) -> pulumi.Input[Union[_builtins.str, RequestTypes]]: ...
    @request_type.setter
    def request_type(self, value: pulumi.Input[Union[_builtins.str, RequestTypes]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionRequestName")
    def action_request_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_request_name.setter
    def action_request_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preReleaseAccessRequestSpec")
    def pre_release_access_request_spec(
        self,
    ) -> Optional[pulumi.Input[PreReleaseAccessRequestSpecArgs]]: ...
    @pre_release_access_request_spec.setter
    def pre_release_access_request_spec(
        self, value: Optional[pulumi.Input[PreReleaseAccessRequestSpecArgs]]
    ): ...

@pulumi.type_token("azure-native:testbase:ActionRequest")
class ActionRequest(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action_request_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_release_access_request_spec: Optional[
            pulumi.Input[
                Union[
                    PreReleaseAccessRequestSpecArgs, PreReleaseAccessRequestSpecArgsDict
                ]
            ]
        ] = ...,
        request_type: Optional[pulumi.Input[Union[_builtins.str, RequestTypes]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ActionRequestArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ActionRequest: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preReleaseAccessRequestSpec")
    def pre_release_access_request_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.PreReleaseAccessRequestSpecResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestType")
    def request_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
