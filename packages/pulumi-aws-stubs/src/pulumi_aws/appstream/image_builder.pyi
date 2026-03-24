

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ImageBuilderArgs', 'ImageBuilder']
@pulumi.input_type
class ImageBuilderArgs:
    def __init__(__self__, *, instance_type: pulumi.Input[_builtins.str], access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]] = ..., appstream_agent_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[ImageBuilderVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]]:
        
        ...
    
    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @appstream_agent_version.setter
    def appstream_agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]]:
        
        ...
    
    @domain_join_info.setter
    def domain_join_info(self, value: Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_default_internet_access.setter
    def enable_default_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_arn.setter
    def image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ImageBuilderVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ImageBuilderVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ImageBuilderState:
    def __init__(__self__, *, access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]] = ..., appstream_agent_version: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[ImageBuilderVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]]:
        
        ...
    
    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageBuilderAccessEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @appstream_agent_version.setter
    def appstream_agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]]:
        
        ...
    
    @domain_join_info.setter
    def domain_join_info(self, value: Optional[pulumi.Input[ImageBuilderDomainJoinInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_default_internet_access.setter
    def enable_default_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_arn.setter
    def image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ImageBuilderVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ImageBuilderVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:appstream/imageBuilder:ImageBuilder")
class ImageBuilder(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageBuilderAccessEndpointArgs, ImageBuilderAccessEndpointArgsDict]]]]] = ..., appstream_agent_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[Union[ImageBuilderDomainJoinInfoArgs, ImageBuilderDomainJoinInfoArgsDict]]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[ImageBuilderVpcConfigArgs, ImageBuilderVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ImageBuilderArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageBuilderAccessEndpointArgs, ImageBuilderAccessEndpointArgsDict]]]]] = ..., appstream_agent_version: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[Union[ImageBuilderDomainJoinInfoArgs, ImageBuilderDomainJoinInfoArgsDict]]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[ImageBuilderVpcConfigArgs, ImageBuilderVpcConfigArgsDict]]] = ...) -> ImageBuilder:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.ImageBuilderAccessEndpoint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> pulumi.Output[outputs.ImageBuilderDomainJoinInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[outputs.ImageBuilderVpcConfig]:
        
        ...
    


