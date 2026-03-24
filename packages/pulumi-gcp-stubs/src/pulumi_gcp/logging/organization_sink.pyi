

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationSinkArgs', 'OrganizationSink']
@pulumi.input_type
class OrganizationSinkArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], bigquery_options: Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]]:
        
        ...
    
    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_children.setter
    def include_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @intercept_children.setter
    def intercept_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationSinkState:
    def __init__(__self__, *, bigquery_options: Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., writer_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]]:
        
        ...
    
    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input[OrganizationSinkBigqueryOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationSinkExclusionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_children.setter
    def include_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @intercept_children.setter
    def intercept_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @writer_identity.setter
    def writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:logging/organizationSink:OrganizationSink")
class OrganizationSink(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bigquery_options: Optional[pulumi.Input[Union[OrganizationSinkBigqueryOptionsArgs, OrganizationSinkBigqueryOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OrganizationSinkExclusionArgs, OrganizationSinkExclusionArgsDict]]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationSinkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bigquery_options: Optional[pulumi.Input[Union[OrganizationSinkBigqueryOptionsArgs, OrganizationSinkBigqueryOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OrganizationSinkExclusionArgs, OrganizationSinkExclusionArgsDict]]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., writer_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> OrganizationSink:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> pulumi.Output[outputs.OrganizationSinkBigqueryOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> pulumi.Output[Optional[Sequence[outputs.OrganizationSinkExclusion]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


