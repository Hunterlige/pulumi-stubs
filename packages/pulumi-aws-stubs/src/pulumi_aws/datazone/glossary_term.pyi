

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GlossaryTermArgs', 'GlossaryTerm']
@pulumi.input_type
class GlossaryTermArgs:
    def __init__(__self__, *, glossary_identifier: pulumi.Input[_builtins.str], domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., term_relations: Optional[pulumi.Input[GlossaryTermTermRelationsArgs]] = ..., timeouts: Optional[pulumi.Input[GlossaryTermTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryIdentifier")
    def glossary_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @glossary_identifier.setter
    def glossary_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="termRelations")
    def term_relations(self) -> Optional[pulumi.Input[GlossaryTermTermRelationsArgs]]:
        
        ...
    
    @term_relations.setter
    def term_relations(self, value: Optional[pulumi.Input[GlossaryTermTermRelationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GlossaryTermTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GlossaryTermTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _GlossaryTermState:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., glossary_identifier: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., term_relations: Optional[pulumi.Input[GlossaryTermTermRelationsArgs]] = ..., timeouts: Optional[pulumi.Input[GlossaryTermTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryIdentifier")
    def glossary_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @glossary_identifier.setter
    def glossary_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="termRelations")
    def term_relations(self) -> Optional[pulumi.Input[GlossaryTermTermRelationsArgs]]:
        
        ...
    
    @term_relations.setter
    def term_relations(self, value: Optional[pulumi.Input[GlossaryTermTermRelationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GlossaryTermTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GlossaryTermTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:datazone/glossaryTerm:GlossaryTerm")
class GlossaryTerm(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., glossary_identifier: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., term_relations: Optional[pulumi.Input[Union[GlossaryTermTermRelationsArgs, GlossaryTermTermRelationsArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[GlossaryTermTimeoutsArgs, GlossaryTermTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GlossaryTermArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., domain_identifier: Optional[pulumi.Input[_builtins.str]] = ..., glossary_identifier: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., term_relations: Optional[pulumi.Input[Union[GlossaryTermTermRelationsArgs, GlossaryTermTermRelationsArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[GlossaryTermTimeoutsArgs, GlossaryTermTimeoutsArgsDict]]] = ...) -> GlossaryTerm:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glossaryIdentifier")
    def glossary_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="termRelations")
    def term_relations(self) -> pulumi.Output[Optional[outputs.GlossaryTermTermRelations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.GlossaryTermTimeouts]]:
        ...
    


