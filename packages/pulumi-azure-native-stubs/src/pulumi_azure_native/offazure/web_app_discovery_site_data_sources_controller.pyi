import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "WebAppDiscoverySiteDataSourcesControllerArgs",
    "WebAppDiscoverySiteDataSourcesController",
]

@pulumi.input_type
class WebAppDiscoverySiteDataSourcesControllerArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        site_name: pulumi.Input[_builtins.str],
        web_app_site_name: pulumi.Input[_builtins.str],
        discovery_site_data_source_name: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]: ...
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> pulumi.Input[_builtins.str]: ...
    @web_app_site_name.setter
    def web_app_site_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteDataSourceName")
    def discovery_site_data_source_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_site_data_source_name.setter
    def discovery_site_data_source_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WebAppDiscoverySiteDataSourcesController(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        discovery_site_data_source_name: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAppDiscoverySiteDataSourcesControllerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebAppDiscoverySiteDataSourcesController: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
