import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegionNetworkEndpointGroupArgs", "RegionNetworkEndpointGroup"]

@pulumi.input_type
class RegionNetworkEndpointGroupArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        app_engine: Optional[
            pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]
        ] = ...,
        cloud_function: Optional[
            pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]
        ] = ...,
        cloud_run: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_data: Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]] = ...,
        psc_target_service: Optional[pulumi.Input[_builtins.str]] = ...,
        serverless_deployment: Optional[
            pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appEngine")
    def app_engine(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]]: ...
    @app_engine.setter
    def app_engine(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]]: ...
    @cloud_function.setter
    def cloud_function(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudRun")
    def cloud_run(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]]: ...
    @cloud_run.setter
    def cloud_run(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_endpoint_type.setter
    def network_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscData")
    def psc_data(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]]: ...
    @psc_data.setter
    def psc_data(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscTargetService")
    def psc_target_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_target_service.setter
    def psc_target_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverlessDeployment")
    def serverless_deployment(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]]: ...
    @serverless_deployment.setter
    def serverless_deployment(
        self,
        value: Optional[
            pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RegionNetworkEndpointGroupState:
    def __init__(
        __self__,
        *,
        app_engine: Optional[
            pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]
        ] = ...,
        cloud_function: Optional[
            pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]
        ] = ...,
        cloud_run: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_data: Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]] = ...,
        psc_target_service: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        serverless_deployment: Optional[
            pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngine")
    def app_engine(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]]: ...
    @app_engine.setter
    def app_engine(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupAppEngineArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]]: ...
    @cloud_function.setter
    def cloud_function(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudFunctionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudRun")
    def cloud_run(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]]: ...
    @cloud_run.setter
    def cloud_run(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupCloudRunArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_endpoint_type.setter
    def network_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscData")
    def psc_data(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]]: ...
    @psc_data.setter
    def psc_data(
        self, value: Optional[pulumi.Input[RegionNetworkEndpointGroupPscDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscTargetService")
    def psc_target_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_target_service.setter
    def psc_target_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverlessDeployment")
    def serverless_deployment(
        self,
    ) -> Optional[pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]]: ...
    @serverless_deployment.setter
    def serverless_deployment(
        self,
        value: Optional[
            pulumi.Input[RegionNetworkEndpointGroupServerlessDeploymentArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class RegionNetworkEndpointGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupAppEngineArgs,
                    RegionNetworkEndpointGroupAppEngineArgsDict,
                ]
            ]
        ] = ...,
        cloud_function: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupCloudFunctionArgs,
                    RegionNetworkEndpointGroupCloudFunctionArgsDict,
                ]
            ]
        ] = ...,
        cloud_run: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupCloudRunArgs,
                    RegionNetworkEndpointGroupCloudRunArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_data: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupPscDataArgs,
                    RegionNetworkEndpointGroupPscDataArgsDict,
                ]
            ]
        ] = ...,
        psc_target_service: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        serverless_deployment: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupServerlessDeploymentArgs,
                    RegionNetworkEndpointGroupServerlessDeploymentArgsDict,
                ]
            ]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegionNetworkEndpointGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupAppEngineArgs,
                    RegionNetworkEndpointGroupAppEngineArgsDict,
                ]
            ]
        ] = ...,
        cloud_function: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupCloudFunctionArgs,
                    RegionNetworkEndpointGroupCloudFunctionArgsDict,
                ]
            ]
        ] = ...,
        cloud_run: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupCloudRunArgs,
                    RegionNetworkEndpointGroupCloudRunArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_data: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupPscDataArgs,
                    RegionNetworkEndpointGroupPscDataArgsDict,
                ]
            ]
        ] = ...,
        psc_target_service: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        serverless_deployment: Optional[
            pulumi.Input[
                Union[
                    RegionNetworkEndpointGroupServerlessDeploymentArgs,
                    RegionNetworkEndpointGroupServerlessDeploymentArgsDict,
                ]
            ]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RegionNetworkEndpointGroup: ...
    @_builtins.property
    @pulumi.getter(name="appEngine")
    def app_engine(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionNetworkEndpointGroupAppEngine]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionNetworkEndpointGroupCloudFunction]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudRun")
    def cloud_run(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionNetworkEndpointGroupCloudRun]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscData")
    def psc_data(self) -> pulumi.Output[outputs.RegionNetworkEndpointGroupPscData]: ...
    @_builtins.property
    @pulumi.getter(name="pscTargetService")
    def psc_target_service(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessDeployment")
    def serverless_deployment(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RegionNetworkEndpointGroupServerlessDeployment]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[Optional[_builtins.str]]: ...
