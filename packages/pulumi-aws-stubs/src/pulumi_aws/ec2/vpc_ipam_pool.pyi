import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcIpamPoolArgs", "VpcIpamPool"]

@pulumi.input_type
class VpcIpamPoolArgs:
    def __init__(
        __self__,
        *,
        address_family: pulumi.Input[_builtins.str],
        ipam_scope_id: pulumi.Input[_builtins.str],
        allocation_default_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_max_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_min_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        aws_service: Optional[pulumi.Input[_builtins.str]] = ...,
        cascade: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_advertisable: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource: Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input[_builtins.str]: ...
    @address_family.setter
    def address_family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeId")
    def ipam_scope_id(self) -> pulumi.Input[_builtins.str]: ...
    @ipam_scope_id.setter
    def ipam_scope_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_default_netmask_length.setter
    def allocation_default_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_max_netmask_length.setter
    def allocation_max_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_min_netmask_length.setter
    def allocation_min_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationResourceTags")
    def allocation_resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @allocation_resource_tags.setter
    def allocation_resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoImport")
    def auto_import(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_import.setter
    def auto_import(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="awsService")
    def aws_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_service.setter
    def aws_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cascade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpSource")
    def public_ip_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_source.setter
    def public_ip_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAdvertisable")
    def publicly_advertisable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_advertisable.setter
    def publicly_advertisable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_ipam_pool_id.setter
    def source_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResource")
    def source_resource(
        self,
    ) -> Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]]: ...
    @source_resource.setter
    def source_resource(
        self, value: Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _VpcIpamPoolState:
    def __init__(
        __self__,
        *,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        allocation_default_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_max_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_min_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        aws_service: Optional[pulumi.Input[_builtins.str]] = ...,
        cascade: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_scope_type: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        pool_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        public_ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_advertisable: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource: Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_default_netmask_length.setter
    def allocation_default_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_max_netmask_length.setter
    def allocation_max_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocation_min_netmask_length.setter
    def allocation_min_netmask_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationResourceTags")
    def allocation_resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @allocation_resource_tags.setter
    def allocation_resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoImport")
    def auto_import(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_import.setter
    def auto_import(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="awsService")
    def aws_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_service.setter
    def aws_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cascade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeId")
    def ipam_scope_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipam_scope_id.setter
    def ipam_scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeType")
    def ipam_scope_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipam_scope_type.setter
    def ipam_scope_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="poolDepth")
    def pool_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pool_depth.setter
    def pool_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpSource")
    def public_ip_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_source.setter
    def public_ip_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAdvertisable")
    def publicly_advertisable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_advertisable.setter
    def publicly_advertisable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_ipam_pool_id.setter
    def source_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResource")
    def source_resource(
        self,
    ) -> Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]]: ...
    @source_resource.setter
    def source_resource(
        self, value: Optional[pulumi.Input[VpcIpamPoolSourceResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:ec2/vpcIpamPool:VpcIpamPool")
class VpcIpamPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        allocation_default_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_max_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_min_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        aws_service: Optional[pulumi.Input[_builtins.str]] = ...,
        cascade: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_advertisable: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource: Optional[
            pulumi.Input[
                Union[VpcIpamPoolSourceResourceArgs, VpcIpamPoolSourceResourceArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcIpamPoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        allocation_default_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_max_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_min_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        allocation_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        aws_service: Optional[pulumi.Input[_builtins.str]] = ...,
        cascade: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_scope_type: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        pool_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        public_ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_advertisable: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource: Optional[
            pulumi.Input[
                Union[VpcIpamPoolSourceResourceArgs, VpcIpamPoolSourceResourceArgsDict]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> VpcIpamPool: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="allocationResourceTags")
    def allocation_resource_tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoImport")
    def auto_import(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="awsService")
    def aws_service(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cascade(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeId")
    def ipam_scope_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipamScopeType")
    def ipam_scope_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="poolDepth")
    def pool_depth(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpSource")
    def public_ip_source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAdvertisable")
    def publicly_advertisable(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceResource")
    def source_resource(
        self,
    ) -> pulumi.Output[Optional[outputs.VpcIpamPoolSourceResource]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
