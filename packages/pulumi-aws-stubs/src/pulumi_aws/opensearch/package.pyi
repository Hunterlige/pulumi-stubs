import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PackageArgs", "Package"]

@pulumi.input_type
class PackageArgs:
    def __init__(
        __self__,
        *,
        package_name: pulumi.Input[_builtins.str],
        package_source: pulumi.Input[PackagePackageSourceArgs],
        package_type: pulumi.Input[_builtins.str],
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        package_description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> pulumi.Input[_builtins.str]: ...
    @package_name.setter
    def package_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="packageSource")
    def package_source(self) -> pulumi.Input[PackagePackageSourceArgs]: ...
    @package_source.setter
    def package_source(self, value: pulumi.Input[PackagePackageSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Input[_builtins.str]: ...
    @package_type.setter
    def package_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageDescription")
    def package_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_description.setter
    def package_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PackageState:
    def __init__(
        __self__,
        *,
        available_package_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        package_description: Optional[pulumi.Input[_builtins.str]] = ...,
        package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_source: Optional[pulumi.Input[PackagePackageSourceArgs]] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availablePackageVersion")
    def available_package_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_package_version.setter
    def available_package_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageDescription")
    def package_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_description.setter
    def package_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_id.setter
    def package_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_name.setter
    def package_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageSource")
    def package_source(self) -> Optional[pulumi.Input[PackagePackageSourceArgs]]: ...
    @package_source.setter
    def package_source(
        self, value: Optional[pulumi.Input[PackagePackageSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_type.setter
    def package_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:opensearch/package:Package")
class Package(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        package_description: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_source: Optional[
            pulumi.Input[Union[PackagePackageSourceArgs, PackagePackageSourceArgsDict]]
        ] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PackageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        available_package_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        package_description: Optional[pulumi.Input[_builtins.str]] = ...,
        package_id: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_source: Optional[
            pulumi.Input[Union[PackagePackageSourceArgs, PackagePackageSourceArgsDict]]
        ] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Package: ...
    @_builtins.property
    @pulumi.getter(name="availablePackageVersion")
    def available_package_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="packageDescription")
    def package_description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageSource")
    def package_source(self) -> pulumi.Output[outputs.PackagePackageSource]: ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
