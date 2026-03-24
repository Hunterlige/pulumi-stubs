

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
__all__ = ['LinkArgs', 'Link']
@pulumi.input_type
class LinkArgs:
    def __init__(__self__, *, label_template: pulumi.Input[_builtins.str], resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], sink_identifier: pulumi.Input[_builtins.str], link_configuration: Optional[pulumi.Input[LinkLinkConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @label_template.setter
    def label_template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sink_identifier.setter
    def sink_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkConfiguration")
    def link_configuration(self) -> Optional[pulumi.Input[LinkLinkConfigurationArgs]]:
        
        ...
    
    @link_configuration.setter
    def link_configuration(self, value: Optional[pulumi.Input[LinkLinkConfigurationArgs]]): # -> None:
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
    


@pulumi.input_type
class _LinkState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., label_template: Optional[pulumi.Input[_builtins.str]] = ..., link_configuration: Optional[pulumi.Input[LinkLinkConfigurationArgs]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sink_arn: Optional[pulumi.Input[_builtins.str]] = ..., sink_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label_template.setter
    def label_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkConfiguration")
    def link_configuration(self) -> Optional[pulumi.Input[LinkLinkConfigurationArgs]]:
        
        ...
    
    @link_configuration.setter
    def link_configuration(self, value: Optional[pulumi.Input[LinkLinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkArn")
    def sink_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sink_arn.setter
    def sink_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sink_identifier.setter
    def sink_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:oam/link:Link")
class Link(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., label_template: Optional[pulumi.Input[_builtins.str]] = ..., link_configuration: Optional[pulumi.Input[Union[LinkLinkConfigurationArgs, LinkLinkConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sink_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LinkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., label_template: Optional[pulumi.Input[_builtins.str]] = ..., link_configuration: Optional[pulumi.Input[Union[LinkLinkConfigurationArgs, LinkLinkConfigurationArgsDict]]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sink_arn: Optional[pulumi.Input[_builtins.str]] = ..., sink_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Link:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkConfiguration")
    def link_configuration(self) -> pulumi.Output[Optional[outputs.LinkLinkConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkArn")
    def sink_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    


