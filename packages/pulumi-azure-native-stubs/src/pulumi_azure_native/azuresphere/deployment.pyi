import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DeploymentArgs", "Deployment"]

@pulumi.input_type
class DeploymentArgs:
    def __init__(
        __self__,
        *,
        catalog_name: pulumi.Input[_builtins.str],
        device_group_name: pulumi.Input[_builtins.str],
        product_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        deployed_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageArgs]]]
        ] = ...,
        deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[_builtins.str]: ...
    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deviceGroupName")
    def device_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_group_name.setter
    def device_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Input[_builtins.str]: ...
    @product_name.setter
    def product_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deployedImages")
    def deployed_images(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageArgs]]]]: ...
    @deployed_images.setter
    def deployed_images(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:azuresphere:Deployment")
class Deployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
        deployed_images: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[ImageArgs, ImageArgsDict]]]]
        ] = ...,
        deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        device_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DeploymentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Deployment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deployedImages")
    def deployed_images(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ImageResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentDateUtc")
    def deployment_date_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
