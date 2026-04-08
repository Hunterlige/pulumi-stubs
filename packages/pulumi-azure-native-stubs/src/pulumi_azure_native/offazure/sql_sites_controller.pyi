import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SqlSitesControllerArgs", "SqlSitesController"]

@pulumi.input_type
class SqlSitesControllerArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        site_name: pulumi.Input[_builtins.str],
        discovery_scenario: Optional[
            pulumi.Input[Union[_builtins.str, SqlSitePropertiesDiscoveryScenario]]
        ] = ...,
        site_appliance_properties_collection: Optional[
            pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]
        ] = ...,
        sql_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, SqlSitePropertiesDiscoveryScenario]]
    ]: ...
    @discovery_scenario.setter
    def discovery_scenario(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SqlSitePropertiesDiscoveryScenario]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]
    ]: ...
    @site_appliance_properties_collection.setter
    def site_appliance_properties_collection(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlSiteName")
    def sql_site_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_site_name.setter
    def sql_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:offazure:SqlSitesController")
class SqlSitesController(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        discovery_scenario: Optional[
            pulumi.Input[Union[_builtins.str, SqlSitePropertiesDiscoveryScenario]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        site_appliance_properties_collection: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SiteAppliancePropertiesArgs, SiteAppliancePropertiesArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SqlSitesControllerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SqlSitesController: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SiteAppliancePropertiesResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
